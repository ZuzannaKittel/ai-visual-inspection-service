from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

from app.core.config import get_settings
from app.core.logging import setup_logging
from app.api.routes import health
from app.api.routes import predict
from app.services.ml_service import MLService
from app.db.base import Base
from app.db.session import engine


settings = get_settings()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("Starting application...")

    # Initialize ML service and store in app state for access in routes
    app.state.ml_service = MLService()

    yield
    logger.info("Shutting down application...")


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    lifespan=lifespan,
)

app.include_router(health.router)
app.include_router(predict.router)
