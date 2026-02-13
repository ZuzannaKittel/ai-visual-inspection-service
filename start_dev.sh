#!/bin/bash

echo "🚀 Starting AI Visual Inspection Service..."

brew services start postgresql@14

echo "⏳ Waiting for PostgreSQL to be ready..."
sleep 3

source venv/bin/activate

uvicorn app.main:app --reload


