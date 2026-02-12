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

    def predict(self, image: Image.Image) -> dict:
        tensor = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, predicted_class = torch.max(probabilities, dim=1)

        return {
            "class": self.classes[predicted_class.item()],
            "confidence": float(confidence.item()),
        }
