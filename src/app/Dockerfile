# Description: This Dockerfile builds the image for the front end application.
#
# Building a New Image:
#   Switch to the src/app directory, then run the command:
#       docker build -t frontend-game-recommender .
#
# Running Image:
#   Switch to the project's root directory where the .env file exists, then run the command:
#       docker run -p 5173:5173 frontend-game-recommender
#
# Pushing a New Image:
#   After confirming that the new image is running as expected, push the new image with the command:
#       docker push freakynoblegas/game-recommender

# Use an official Node 18.17.0
FROM node:18.17.0

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json yarn.lock vite.config.js babel.config.cjs ./

# Install app dependencies
RUN yarn install

# Build app
RUN yarn build

# Change directory to build
WORKDIR  /dist

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
