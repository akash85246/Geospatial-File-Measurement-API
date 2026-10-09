import logging
import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session

from . import models, schemas, services
from .database import Base, engine, get_db
from .landing import render_landing

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = (".kml", ".zip")

PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "").rstrip("/")


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Geospatial File Measurement API",
    description="Upload a KML or zipped Shapefile and get per-feature area / length measurements.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    base_url = PUBLIC_BASE_URL or str(request.base_url).rstrip("/")
    return render_landing(base_url)


def _get_file_or_404(db: Session, file_id: str) -> models.UploadedFile:
    record = db.get(models.UploadedFile, file_id)
    if record is None:
        raise HTTPException(status_code=404, detail="File not found")
    return record


def _fail(db: Session, record: models.UploadedFile, message: str, status_code: int) -> JSONResponse:
    """Persist the failure on the file record and return it to the client."""
    record.status = "FAILED"
    record.error_message = message
    db.commit()
    return JSONResponse(
        status_code=status_code,
        content={"id": record.id, "status": "FAILED", "error_message": message},
    )


@app.post(
    "/api/files/",
    status_code=201,
    response_model=schemas.FileOut,
    responses={400: {"model": schemas.FailureOut}, 500: {"model": schemas.FailureOut}},
)
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    filename = file.filename or ""
    if not filename.lower().endswith(ALLOWED_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Only .kml or .zip (containing a Shapefile) files are supported")

    record = models.UploadedFile(filename=filename, status="PROCESSING")
    db.add(record)
    db.commit()

    try:
        features, crs = services.process_file(file)
        record.crs = crs
        record.feature_count = len(features)
        record.features = [models.Feature(**f) for f in features]
        record.status = "COMPLETED"
        db.commit()
    except services.ParserError as exc:
        db.rollback()
        return _fail(db, record, str(exc), 400)
    except Exception:
        logger.exception("Unexpected error while processing %s", filename)
        db.rollback()
        return _fail(db, record, "Unexpected error while processing the file", 500)

    db.refresh(record)
    return record


@app.get("/api/files/{file_id}/", response_model=schemas.FileOut)
def get_file(file_id: str, db: Session = Depends(get_db)):
    return _get_file_or_404(db, file_id)


@app.get("/api/files/{file_id}/measurements/", response_model=schemas.MeasurementsResponse)
def get_measurements(file_id: str, db: Session = Depends(get_db)):
    record = _get_file_or_404(db, file_id)
    if record.status != "COMPLETED":
        raise HTTPException(status_code=409, detail=f"File is {record.status}; no measurements available")
    return {
        "file_id": record.id,
        "count": len(record.features),
        "measurements": [
            {
                "feature_index": f.feature_index,
                "geometry_type": f.geometry_type,
                "crs": f.crs,
                "measurement_type": f.measurement_type,
                "value": f.measurement_value,
                "unit": f.measurement_unit,
                "note": f.note,
            }
            for f in record.features
        ],
    }


@app.get("/api/files/{file_id}/features/", response_model=schemas.FeaturesResponse)
def get_features(file_id: str, db: Session = Depends(get_db)):
    record = _get_file_or_404(db, file_id)
    if record.status != "COMPLETED":
        raise HTTPException(status_code=409, detail=f"File is {record.status}; no features available")
    return {
        "file_id": record.id,
        "count": len(record.features),
        "features": [
            {
                "feature_index": f.feature_index,
                "geometry_type": f.geometry_type,
                "geometry_wkt": f.geometry_wkt,
                "crs": f.crs,
                "properties": f.properties or {},
            }
            for f in record.features
        ],
    }