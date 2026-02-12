# AI Visual Inspection Service

A production-ready FastAPI microservice for image classification with a pretrained CNN, structured logging, and persistent storage.

## Features (Implemented Today)

- **FastAPI backend** with clean layered architecture
- **Pretrained CNN inference** using `EfficientNet-B0`  
  - Top-k predictions (default: 3)  
  - Softmax confidence scores
- **Structured logging** for startup, inference, and shutdown
- **PostgreSQL integration**  
  - Stores top-1 prediction per request
  - SQLAlchemy 2.0 ORM  
  - Automatic table creation on startup (dev mode)
- **OpenAPI documentation** via `/docs`
- **Clean response schemas** using PydanticProduction-style ML microservice built with:

- FastAPI
- PyTorch
- PostgreSQL
- Docker

## Goal

Demonstrate clean architecture for deploying ML models as scalable API services.

## Status

🚧 In development

