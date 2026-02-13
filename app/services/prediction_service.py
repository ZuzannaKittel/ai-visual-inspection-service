from sqlalchemy.orm import Session
from app.models.prediction import Prediction


class PredictionService:

    @staticmethod
    def save_prediction(
        db: Session,
        model_name: str,
        model_version: str,
        class_name: str,
        confidence: float,
    ) -> Prediction:

        db_prediction = Prediction(
            model_name=model_name,
            model_version=model_version,
            class_name=class_name,
            confidence=confidence,
        )

        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)

        return db_prediction

    @staticmethod
    def get_predictions(db: Session):
        return db.query(Prediction).order_by(Prediction.created_at.desc()).all()
