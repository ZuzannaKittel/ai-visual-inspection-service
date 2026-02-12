import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import logging


logger = logging.getLogger(__name__)


class MLService:
    def __init__(self):
        logger.info("Loading pretrained model...")
        self.model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=models.ResNet18_Weights.DEFAULT.meta["mean"],
                std=models.ResNet18_Weights.DEFAULT.meta["std"],
            ),
        ])

        self.classes = models.ResNet18_Weights.DEFAULT.meta["categories"]

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
