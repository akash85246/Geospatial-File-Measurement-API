"""Geometry and CRS helpers. Pure functions: no file I/O, no measurement rules.

CRS strategy
------------
* Geographic CRS (e.g. EPSG:4326): each geometry is reprojected to the UTM zone
  of its own centroid (EPSG:326xx north / 327xx south, UPS near the poles), so
  distances and areas are computed in metres, never in degrees.
* Projected CRS (e.g. a state-plane Shapefile): geometry is left in its native
  CRS and a scale factor converts the CRS axis unit (feet, etc.) to metres.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any

import shapely
from pyproj import CRS, Transformer
from shapely.ops import transform as shapely_transform


def crs_label(crs: CRS) -> str:
    """Human-readable CRS id, e.g. 'EPSG:4326'. Falls back to the CRS name."""
    authority = crs.to_authority(min_confidence=70)
    return f"{authority[0]}:{authority[1]}" if authority else (crs.name or "UNKNOWN")


def utm_epsg(lon: float, lat: float) -> int:
    """EPSG code of the UTM zone for a lon/lat (UPS polar stereographic beyond 84N / 80S)."""
    if lat > 84:
        return 32661
    if lat < -80:
        return 32761
    zone = min(max(int((lon + 180) // 6) + 1, 1), 60)
    return (32600 if lat >= 0 else 32700) + zone


@lru_cache(maxsize=128)
def _wgs84_to_utm(epsg: int) -> Transformer:
    return Transformer.from_crs(4326, epsg, always_xy=True)


def unit_factor_to_metres(crs: CRS) -> float:
    """Metres per CRS axis unit (1.0 for metre, 0.3048 for foot, ...)."""
    try:
        factor = crs.axis_info[0].unit_conversion_factor
        return float(factor) if factor else 1.0
    except Exception:
        return 1.0


def to_2d(geom: Any) -> Any:
    """Drop Z values (KML often carries altitude). Requires shapely >= 2.0."""
    return shapely.force_2d(geom)


class MetricProjector:
    """Brings geometries of one CRS into a metric space.

    After ``project(geom)``, multiply lengths by ``scale`` and areas by
    ``scale ** 2`` to get metres / square metres.
    """

    def __init__(self, crs: CRS) -> None:
        self.crs = crs
        self.geographic = bool(crs.is_geographic)
        self.scale = 1.0 if self.geographic else unit_factor_to_metres(crs)
        self._to_wgs84 = (
            Transformer.from_crs(crs, 4326, always_xy=True) if self.geographic else None
        )

    def project(self, geom: Any) -> Any:
        if not self.geographic:
            return geom
        geom_wgs84 = shapely_transform(self._to_wgs84.transform, geom)
        centroid = geom_wgs84.centroid
        transformer = _wgs84_to_utm(utm_epsg(centroid.x, centroid.y))
        return shapely_transform(transformer.transform, geom_wgs84)