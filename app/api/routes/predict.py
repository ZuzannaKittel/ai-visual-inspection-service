from fastapi import APIRouter, UploadFile, File, Request
from PIL import Image
import io

from app.schemas.prediction_schema import PredictionResponse
from app.db.session import SessionLocal
from app.models.prediction import Prediction

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_image(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    ml_service = request.app.state.ml_service
    result = ml_service.predict(image)

    # Save top-1 prediction
    top_prediction = result["predictions"][0]

    db = SessionLocal()
    try:
        db_prediction = Prediction(
            model_name=result["model_name"],
            model_version=result["model_version"],
            class_name=top_prediction["class_name"],
            confidence=top_prediction["confidence"],
        )
        db.add(db_prediction)
        db.commit()
    finally:
        db.close()

    return result

