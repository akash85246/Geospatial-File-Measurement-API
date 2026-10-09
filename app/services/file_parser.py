from __future__ import annotations

import logging
import math
import tempfile
import zipfile
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import geopandas as gpd
import numpy as np
import pandas as pd
import pyogrio
from pyproj import CRS

from .geometry import MetricProjector, crs_label, to_2d
from .measurement import measure_geometry

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {".kml", ".zip"}
MAX_UPLOAD_BYTES = 50 * 1024 * 1024            # 50 MB upload
MAX_UNCOMPRESSED_BYTES = 200 * 1024 * 1024     # zip-bomb guard
_CHUNK = 1024 * 1024

Frame = Tuple[gpd.GeoDataFrame, Optional[str]]  # (data, note about CRS assumptions)


class ParserError(Exception):
    """Problem with the uploaded file (bad type, corrupt, no data...). Map to HTTP 400."""
def process_file(upload: Any) -> Tuple[List[Dict[str, Any]], str]:
    """Process a FastAPI ``UploadFile`` (anything with ``.filename`` and ``.file``)."""
    suffix = Path(upload.filename or "").suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ParserError("Unsupported file type. Upload a .kml or a .zip containing a Shapefile.")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        saved = tmp_path / f"upload{suffix}"
        _save_stream(upload.file, saved)

        if suffix == ".zip":
            frames = _read_shapefile_zip(saved, tmp_path / "extracted")
        else:
            frames = _read_kml(saved)

    features = _build_features(frames)
    if not features:
        raise ParserError("No features found in the file.")

    labels = {f["crs"] for f in features}
    file_crs = labels.pop() if len(labels) == 1 else "MIXED"
    return features, file_crs

def _save_stream(stream: Any, dest: Path) -> None:
    """Copy the upload to disk in chunks, enforcing the size limit."""
    written = 0
    with open(dest, "wb") as out:
        while True:
            chunk = stream.read(_CHUNK)
            if not chunk:
                break
            written += len(chunk)
            if written > MAX_UPLOAD_BYTES:
                raise ParserError(f"File too large (limit {MAX_UPLOAD_BYTES // (1024 * 1024)} MB).")
            out.write(chunk)
    if written == 0:
        raise ParserError("Uploaded file is empty.")


def _safe_extract(zip_path: Path, dest: Path) -> None:
    """Extract a zip, rejecting zip-slip paths and zip bombs."""
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    try:
        with zipfile.ZipFile(zip_path) as zf:
            infos = zf.infolist()
            if sum(i.file_size for i in infos) > MAX_UNCOMPRESSED_BYTES:
                raise ParserError("Zip archive is too large when uncompressed.")
            for info in infos:
                target = (root / info.filename).resolve()
                if target != root and root not in target.parents:
                    raise ParserError("Zip contains an unsafe path.")
            zf.extractall(root)
    except zipfile.BadZipFile as exc:
        raise ParserError("Invalid or corrupt zip file.") from exc


def _read_shapefile_zip(zip_path: Path, extract_dir: Path) -> List[Frame]:
    _safe_extract(zip_path, extract_dir)

    shp_files = sorted(
        p for p in extract_dir.rglob("*.shp")
        if "__MACOSX" not in p.parts and not p.name.startswith("._")
    )
    if not shp_files:
        raise ParserError("Zip does not contain a .shp file.")

    frames: List[Frame] = []
    for shp in shp_files:
        try:
            gdf = gpd.read_file(shp, engine="pyogrio")
        except Exception as exc:  # missing .shx/.dbf, corrupt data, ...
            raise ParserError(f"Could not read shapefile '{shp.name}': {exc}") from exc
        if gdf.empty:
            continue
        crs, note = _resolve_crs(gdf, is_kml=False)
        frames.append((gdf.set_crs(crs, allow_override=True), note))
    return frames


def _read_kml(kml_path: Path) -> List[Frame]:
    """Read every layer of a KML file (KML folders show up as layers)."""
    try:
        layers = [row[0] for row in pyogrio.list_layers(kml_path)]
    except Exception as exc:
        raise ParserError(f"Could not read KML: {exc}") from exc
    if not layers:
        raise ParserError("KML contains no layers.")

    frames: List[Frame] = []
    for layer in layers:
        try:
            gdf = gpd.read_file(kml_path, layer=layer, engine="pyogrio")
        except Exception as exc:
            logger.warning("Skipping unreadable KML layer %s: %s", layer, exc)
            continue
        if gdf.empty:
            continue
        if len(layers) > 1:
            gdf["layer"] = layer
        crs, note = _resolve_crs(gdf, is_kml=True)
        frames.append((gdf.set_crs(crs, allow_override=True), note))
    return frames


def _resolve_crs(gdf: gpd.GeoDataFrame, is_kml: bool) -> Tuple[CRS, Optional[str]]:
    """Return the CRS to use, assuming EPSG:4326 where that is safe, else erroring."""
    if gdf.crs is not None:
        return CRS.from_user_input(gdf.crs), None
    if is_kml:
        return CRS.from_epsg(4326), "CRS missing; assumed EPSG:4326 (KML standard)"

    minx, miny, maxx, maxy = gdf.total_bounds
    looks_like_lonlat = (
        all(math.isfinite(v) for v in (minx, miny, maxx, maxy))
        and -180 <= minx and maxx <= 180 and -90 <= miny and maxy <= 90
    )
    if looks_like_lonlat:
        return CRS.from_epsg(4326), "CRS missing (.prj not found); coordinates look like lon/lat, assumed EPSG:4326"
    raise ParserError("Shapefile has no CRS (.prj missing) and coordinates do not look like lon/lat.")

def _build_features(frames: List[Frame]) -> List[Dict[str, Any]]:
    features: List[Dict[str, Any]] = []
    index = 0

    for gdf, frame_note in frames:
        crs = CRS.from_user_input(gdf.crs)
        label = crs_label(crs)
        projector = MetricProjector(crs)
        attrs = gdf.drop(columns=gdf.geometry.name).to_dict("records")

        for i, geom in enumerate(gdf.geometry):
            is_empty = geom is None or geom.is_empty
            if not is_empty:
                geom = to_2d(geom)

            m = measure_geometry(None if is_empty else geom, projector)
            
            notes = [n for n in (frame_note, m.note) if n]

            features.append({
                "feature_index": index,
                "geometry_type": "Empty" if is_empty else geom.geom_type,
                "geometry_wkt": None if is_empty else geom.wkt,
                "crs": label,
                "properties": {str(k): _json_safe(v) for k, v in attrs[i].items()},
                "measurement_type": m.measurement_type,
                "measurement_value": m.value,
                "measurement_unit": m.unit,
                "note": "; ".join(notes) if notes else None,
            })
            index += 1

    return features


def _json_safe(value: Any) -> Any:
    """Convert attribute values (numpy / pandas / NaN / bytes) to JSON-serialisable types."""
    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass
    if isinstance(value, np.generic):
        return _json_safe(value.item())
    if isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return str(value)