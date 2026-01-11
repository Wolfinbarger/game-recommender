# Dockerfile for FastAPI Backend
#
# This builds a Docker image for the Game Recommender API server.
# The API uses FastAPI, SQLModel, and uv for dependency management.
#
# Building the image:
#   cd src/api
#   docker build -t game-recommender-api .
#
# Running the container:
#   docker run -p 8000:8000 game-recommender-api
#
# Or use docker-compose.yml from the root directory (recommended):
#   docker compose up

# Use Python 3.11 slim image as base
# Slim images are smaller and have fewer dependencies
FROM python:3.11-slim

# Set working directory to /app
# All subsequent commands will run from this directory
WORKDIR /app

# Copy dependency files first
# This allows Docker to cache the dependency layer
# if only code changes (not dependencies)
COPY pyproject.toml ./

# Install uv (fast Python package manager)
# Then install all project dependencies
RUN pip install uv && \
    uv pip install --system -r pyproject.toml

# Copy the rest of the application code
COPY . .

# Make the entrypoint script executable
# This script runs migrations before starting the server
RUN chmod +x entrypoint.sh

# Expose port 8000 for the FastAPI server
EXPOSE 8000

# Run the entrypoint script when container starts
# This will:
# 1. Run Alembic migrations (alembic upgrade head)
# 2. Start the FastAPI server (uvicorn)
CMD ["./entrypoint.sh"]
