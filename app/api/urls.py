from fastapi import FastAPI

from app.views.files import router as files_router


app = FastAPI(
    title="Geospatial File Measurement API",
)

app.include_router(files_router)