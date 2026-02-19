# AI Visual Inspection Service

## Overview

A containerized AI-powered image classification API built with FastAPI, PyTorch, PostgreSQL, and Docker.
This project demonstrates clean backend architecture, database migrations, model inference handling, and production-style containerization.

## Goal

Demonstrate clean architecture for a production-style microservice for deplyoing ML models as scalable API services.

## Architecture

This project follows a clean, layered backend architecture:
 - **API layer** – FastAPI routers and request/response schemas
 - **Service layer** – ML logic and inference handling
 - **Persistence layer** – SQLAlchemy ORM models and database session management
 - **Infrastructure layer** – Docker, PostgreSQL, Alembic

## Running the Project

1. Build and start services
```sh
docker compose up --build
```
2. Access API documentation
```sh
  http://localhost:8000/docs
```
3. Health check
```sh
  http://localhost:8000/health
```

## Example Prediction Record

```json
{
  "model_name": "efficientnet_b0",
  "model_version": "imagenet-1k",
  "class_name": "sports car",
  "confidence": 0.88
}
```

## Features

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
- **Alembic database migrations**
  - Version-controlled schema management
  - Automatic migration execution on container startup
  - Migration history tracking via alembic_version
- **Dockerized environment**
  - Multi-service setup using Docker Compose
  - Isolated PostgreSQL container
  - Internal service networking (db hostname)
- **Health check endpoint**
  - /health route for service readiness checks
- **Environment-based configuration**
  - DATABASE_URL configurable via environment variables
  - Production-ready configuration pattern
- **Modular project structure**
  - Separation of API, services, models, and database layers
  - Clear dependency boundaries



