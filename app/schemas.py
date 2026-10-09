from typing import Any, Optional

from pydantic import BaseModel, ConfigDict


class FileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    filename: str
    feature_count: int
    crs: Optional[str]
    status: str
    error_message: Optional[str] = None


class MeasurementOut(BaseModel):
    feature_index: int
    geometry_type: str
    crs: Optional[str]
    measurement_type: Optional[str]
    value: Optional[float]
    unit: Optional[str]
    note: Optional[str]


class MeasurementsResponse(BaseModel):
    file_id: str
    count: int
    measurements: list[MeasurementOut]


class FeatureOut(BaseModel):
    feature_index: int
    geometry_type: str
    geometry_wkt: Optional[str]
    crs: Optional[str]
    properties: dict[str, Any]


class FeaturesResponse(BaseModel):
    file_id: str
    count: int
    features: list[FeatureOut]


class FailureOut(BaseModel):
    id: str
    status: str
    error_message: str