# Description: This Dockerfile builds the image for the API server.
#
# Building a New Image:
#   Switch to the src/api directory, then run the command:
#       docker build -t game-recommender .
#
# Running Image:
#   Switch to the project's root directory where the .env file exists, then run the command:
#       docker run --env-file=.env -p 8000:8000 game-recommender
#
# Pushing a New Image:
#   After confirming that the new image is running as expected, push the new image with the command:
#       docker push freakynoblegas/game-recommender:latest

# Use Python 3.9.18 as the base image
FROM python:3.9.18-slim-bookworm

# Used to let the app know which host to use for the database connection
ENV DOCKER_ENABLED="enabled"

# Set the working directory to /app. This automatically creates the app directory in the container and
# cd's to this directory.
WORKDIR /app

# Copy all of the API directory files
COPY . .

# Install the dependencies
RUN pip3 install psycopg2-binary
RUN pip3 install -r requirements.txt

# Django server port
EXPOSE 8000

# Run the Django server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]