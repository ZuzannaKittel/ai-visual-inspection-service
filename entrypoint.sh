#!/bin/sh
set -e

echo "⏳ Waiting for database..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  sleep 1
done

echo "✅ Database ready, running migrations..."
alembic upgrade head

echo "🚀 Starting Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
