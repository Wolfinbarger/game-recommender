# Description: This Dockerfile builds the image for the API server.
#
# Building a New Image:
#   Switch to the src/api directory, then run the command:
#       docker build -t freakynoblegas/game-recommender:api-latest .
#
# Running Image:
#   Switch to the project's root directory where the .env file exists, then run the command:
#       docker run --env-file=.env -p 8000:8000 -p 5432:5432 freakynoblegas/game-recommender:api-latest
#
# Pushing a New Image:
#   After confirming that the new image is running as expected, push the new image with the command:
#       docker push freakynoblegas/game-recommender:api-latest

# Use Python 3.9.18 as the base image
FROM python:3.9.18-slim-bookworm

# Used to let the app know which host to use for the database connection
ENV DOCKER_ENABLED=true

# Set the working directory to /app. This automatically creates the app directory in the container and
# cd's to this directory.
WORKDIR /app

# Copy API source code
COPY . .

# Install the dependencies
RUN pip3 install psycopg2-binary

# Running the app locally doesn't require the binary version of psycopg2. This line removes that dependency while
# installing everything else.
RUN pip3 install $(awk '!/psycopg2/' requirements.txt)

# FastAPI server port
EXPOSE 8000

# Run the FastAPI server when the container starts
CMD ["fastapi", "run", "main.py", "--port", "8000"]