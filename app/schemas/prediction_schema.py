from pydantic import BaseModel, Field
from typing import List


class PredictionItem(BaseModel):
    class_name: str = Field(..., description="Predicted class label")
    confidence: float = Field(..., description="Softmax confidence score")


class PredictionResponse(BaseModel):
    model_name: str = Field(..., description="Model architecture name")
    model_version: str = Field(..., description="Model weight version")
    predictions: List[PredictionItem]
