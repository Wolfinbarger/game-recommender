# Description: This Dockerfile builds the image for the front end application.
#
# Building a New Image:
#   Switch to the src/app directory, then run the command:
#       docker build -t frontend/game-recommender:latest .
#
# Running Image:
#   Switch to the project's root directory where the .env file exists, then run the command:
#       docker run --env-file=.env -p 8000:8000 freakynoblegas/game-recommender:latest
#
# Pushing a New Image:
#   After confirming that the new image is running as expected, push the new image with the command:
#       docker push freakynoblegas/game-recommender:latest

# Use an official Node 18.17.0
FROM node:18.17.0

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json yarn.lock vite.config.js babel.config.cjs ./

# Install app dependencies
RUN yarn install

# Copy all the app directory files
COPY . .

# Expose the port that the app runs on
EXPOSE 5173

# # Define environment variable
# ENV REACT_APP_API_URL=http://localhost:5000

# # Build the app
# RUN vite build

# Command to run the app
CMD ["yarn", "dev"]
