import torch
import torchvision.transforms as transforms
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights
from PIL import Image

import logging


logger = logging.getLogger(__name__)


class MLService:
    def __init__(self):
        logger.info("Loading pretrained EfficientNet-B0 model...")

        weights = EfficientNet_B0_Weights.DEFAULT
        self.model = efficientnet_b0(weights=weights)
        self.model.eval()

        self.transform = weights.transforms()
        self.classes = weights.meta["categories"]

        logger.info("Model loaded successfully.")

    def predict(self, image: Image.Image, top_k: int = 3) -> dict:
        tensor = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)

            top_probs, top_indices = torch.topk(probabilities, top_k)

        predictions = []
        for prob, idx in zip(top_probs[0], top_indices[0]):
            predictions.append({
                "class_name": self.classes[idx.item()],
                "confidence": float(prob.item())
            })

        return {
            "model_name": "efficientnet_b0",
            "model_version": "imagenet-1k",
            "predictions": predictions
        }

