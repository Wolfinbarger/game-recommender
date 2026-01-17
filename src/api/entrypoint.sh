#!/bin/bash

# Entrypoint Script for FastAPI Backend
#
# This script runs when the Docker container starts.
# It performs these steps:
# 1. Wait for database to be ready
# 2. Run database migrations (Alembic)
# 3. Start the FastAPI server (uvicorn)
#
# This ensures the database schema is always up to date
# before the application starts serving requests.

set -e  # Exit immediately if any command fails

echo "Starting Game Recommender API..."

# Debug: Print DATABASE_URL (mask password for security)
if [ -n "$DATABASE_URL" ]; then
    echo "Using DATABASE_URL from environment"
else
    echo "WARNING: DATABASE_URL not set!"
fi

# Wait a few seconds for database to be fully ready
# Even with health checks, sometimes we need a small delay
echo "Waiting for database to be ready..."
sleep 3

# Step 1: Run database migrations
# This applies any pending database schema changes
# "alembic upgrade head" means "upgrade to the latest version"
echo "Running database migrations..."
alembic upgrade head

# Step 2: Start the FastAPI server
# --host 0.0.0.0 makes it accessible from outside the container
# --port 8000 is the port the API listens on
# --reload enables auto-reload when code changes (development mode)
echo "Starting FastAPI server..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
