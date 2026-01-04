# Dockerfile for SvelteKit Frontend
#
# This builds a Docker image for the Game Recommender frontend application.
# The frontend uses SvelteKit, TypeScript, and Bun for package management.
#
# Building the image:
#   cd src/app
#   docker build -t game-recommender-frontend .
#
# Running the container:
#   docker run -p 5173:5173 game-recommender-frontend
#
# Or use compose.yaml from the root directory (recommended):
#   docker compose up

# Use Bun's official Docker image
# Bun is a fast all-in-one JavaScript runtime and package manager
FROM oven/bun:1

# Set working directory
WORKDIR /app

# Copy package files first for better Docker layer caching
# If only code changes (not dependencies), Docker can reuse this layer
COPY package.json bun.lockb* ./

# Install dependencies using Bun
# Bun is much faster than npm/yarn for installing packages
RUN bun install

# Copy the rest of the application code
COPY . .

# Expose port 5173 (Vite's default dev server port)
EXPOSE 5173

# Run the development server
# --host makes the server accessible from outside the container
CMD ["bun", "run", "dev", "--host"]
