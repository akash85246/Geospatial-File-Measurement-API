from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, services
from app.schemas import FileResponse, MeasurementResponse


router = APIRouter(
    prefix="/files",
    tags=["Files"],
)


@router.post(
    "/",
    response_model=FileResponse,
    status_code=201,
)
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required",
        )

    if not file.filename.lower().endswith((".kml", ".zip")):
        raise HTTPException(
            status_code=400,
            detail="Only .kml or .zip (Shapefile) files are supported",
        )

    record = models.UploadedFile(
        filename=file.filename,
        status="PROCESSING",
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    

    try:
        features, crs = services.process_file(file)

        record.crs = crs
        record.feature_count = len(features)

        record.features = [
            models.Feature(**feature)
            for feature in features
        ]

        record.status = "COMPLETED"
        record.error_message = None

        db.commit()
        db.refresh(record)

    except Exception as e:
        db.rollback()

        record = db.get(models.UploadedFile, record.id)

        if record:
            record.status = "FAILED"
            record.error_message = str(e)

            db.commit()
            db.refresh(record)

    return record


@router.get(
    "/{file_id}/",
    response_model=FileResponse,
)
def get_file(
    file_id: str,
    db: Session = Depends(get_db),
):
    record = db.get(models.UploadedFile, file_id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    return record


@router.get(
    "/{file_id}/measurements/",
    response_model=list[MeasurementResponse],
)
def get_measurements(
    file_id: str,
    db: Session = Depends(get_db),
):
    record = db.get(models.UploadedFile, file_id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    return record.features