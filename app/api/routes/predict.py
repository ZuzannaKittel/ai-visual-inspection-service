from fastapi import APIRouter, UploadFile, File, Request
from PIL import Image
import io

from app.schemas.prediction_schema import PredictionResponse
from app.db.session import SessionLocal
from app.models.prediction import Prediction
from typing import List

from fastapi import APIRouter, UploadFile, File, Request, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.services.prediction_service import PredictionService


router = APIRouter()

@router.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_image(
    request: Request,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    ml_service = request.app.state.ml_service
    result = ml_service.predict(image)

    top_prediction = result["predictions"][0]

    PredictionService.save_prediction(
        db=db,
        model_name=result["model_name"],
        model_version=result["model_version"],
        class_name=top_prediction["class_name"],
        confidence=top_prediction["confidence"],
    )

    return result

@router.get("/predictions", tags=["Prediction"])
def list_predictions(db: Session = Depends(get_db)):
    return PredictionService.get_predictions(db)