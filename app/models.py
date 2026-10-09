import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import ForeignKey, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class UploadedFile(Base):
    __tablename__ = "files"

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: uuid.uuid4().hex,
    )
    filename: Mapped[str]
    status: Mapped[str] = mapped_column(
        default="PENDING",
    )
    crs: Mapped[Optional[str]] = mapped_column(
        nullable=True,
    )
    feature_count: Mapped[int] = mapped_column(
        default=0,
    )
    error_message: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
    )
    features: Mapped[list["Feature"]] = relationship(
        back_populates="file",
        cascade="all, delete-orphan",
    )


class Feature(Base):
    __tablename__ = "features"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    file_id: Mapped[str] = mapped_column(
        ForeignKey("files.id"),
        index=True,
    )
    feature_index: Mapped[int]
    geometry_type: Mapped[str]
    geometry_wkt: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    crs: Mapped[Optional[str]] = mapped_column(
        nullable=True,
    )
    properties: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
    )
    measurement_type: Mapped[Optional[str]] = mapped_column(
        nullable=True,
    )
    measurement_value: Mapped[Optional[float]] = mapped_column(
        nullable=True,
    )
    measurement_unit: Mapped[Optional[str]] = mapped_column(
        nullable=True,
    )
    note: Mapped[Optional[str]] = mapped_column(
        nullable=True,
    )
    file: Mapped["UploadedFile"] = relationship(
        back_populates="features",
    )