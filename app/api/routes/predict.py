from fastapi import APIRouter, UploadFile, File, Request
from PIL import Image
import io

router = APIRouter()


@router.post("/predict", tags=["Prediction"])
async def predict_image(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    ml_service = request.app.state.ml_service
    result = ml_service.predict(image)

    return result
