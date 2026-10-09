from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Optional

from .geometry import MetricProjector

logger = logging.getLogger(__name__)

AREA_TYPES = {"Polygon", "MultiPolygon"}
LENGTH_TYPES = {"LineString", "LinearRing", "MultiLineString"}
POINT_TYPES = {"Point", "MultiPoint"}


@dataclass(frozen=True)
class Measurement:
    measurement_type: Optional[str] = None   
    value: Optional[float] = None
    unit: Optional[str] = None             
    note: Optional[str] = None


def measure_geometry(geom: Any, projector: MetricProjector) -> Measurement:
    """Measure one geometry. Failures become a note instead of an exception."""
    if geom is None or geom.is_empty:
        return Measurement(note="Empty or missing geometry")

    try:
        notes = []
        if not geom.is_valid:
            notes.append("Invalid geometry; measurement may be inaccurate")

        geom_type = geom.geom_type
        if geom_type in POINT_TYPES:
            notes.append("No measurement defined for point geometries")
            return Measurement(note="; ".join(notes))
        if geom_type not in AREA_TYPES | LENGTH_TYPES:
            notes.append(f"Unsupported geometry type for measurement: {geom_type}")
            return Measurement(note="; ".join(notes))

        projected = projector.project(geom)
        scale = projector.scale
        note = "; ".join(notes) or None

        if geom_type in AREA_TYPES:
            return Measurement("area", round(projected.area * scale ** 2, 4), "m2", note)
        return Measurement("length", round(projected.length * scale, 4), "m", note)

    except Exception as exc:
        # logger.exception(
        # "Measurement failed for geometry type=%s: %s",
        # getattr(geom, "geom_type", None),
        # exc,
        # )
        return Measurement(
        measurement_type=None,
        value=None,
        unit=None,
        note=f"Measurement failed: {type(exc).__name__}: {exc}",
        )