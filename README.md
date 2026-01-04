# Game Recommender

A full-stack web app that helps you discover awesome games to play with your friends or solo.

## Description

Game Recommender helps users find new games to play, both with friends or solo, by analyzing the user's gaming
preferences and providing results using our enriched dataset. Whether they're looking for a casual party game,
a thrilling adventure game, or a challenging strategy game, this app has them covered. After the user enters their
preferences, this app will show them a list of games that match their criteria.

In our project's future state, they can also read reviews, watch trailers, and compare prices from different platforms.
Our dataset uses multiple data sources, such as datasets on Kaggle, official store APIs, and custom web scrapers.

This project is a full stack application built using the following technologies.

### Frontend

- [SvelteKit](https://kit.svelte.dev/) - Modern reactive web framework with file-based routing
- [TypeScript](https://www.typescriptlang.org/) - Type-safe JavaScript
- [SCSS](https://sass-lang.com/) - CSS preprocessing with variables and nesting
- [Bun](https://bun.sh/) - Fast JavaScript runtime and package manager

### Backend

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework for building APIs
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQL database ORM with Python type hints
- [uv](https://github.com/astral-sh/uv) - Blazingly fast Python package manager
- [PostgreSQL](https://www.postgresql.org/) - Relational database

### Development Tools

- [Docker Compose](https://docs.docker.com/compose/) - Multi-container orchestration
- [Figma](https://www.figma.com/) - UI/UX design and prototyping

## How to run this project locally

### Prerequisites

Before running the project, make sure you have the following installed:

- **For Docker setup**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **For local development**:
  - [Bun](https://bun.sh/) - JavaScript runtime and package manager
  - [uv](https://github.com/astral-sh/uv) - Python package manager
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) - For the database

### Quick Start with Docker (Recommended)

The easiest way to run the entire stack is using Docker Compose:

```bash
# Start all services (database, backend, frontend)
docker compose up

# Or run in detached mode (background)
docker compose up -d

# View logs
docker compose logs -f

# Stop all services
docker compose down
```

**Access the application:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Database: localhost:5432

### Local Development Setup

For active development with hot-reload, you can run the frontend and backend locally:

#### 1. Start the Database

First, start just the PostgreSQL database with Docker:

```bash
docker compose up db -d
```

#### 2. Setup and Run Backend

```bash
# Navigate to the API directory
cd src/api

# Install dependencies (first time only)
uv sync --no-install-project

# Run database migrations (first time only, or when schema changes)
uv run alembic upgrade head

# Start the development server
uv run uvicorn main:app --reload
```

The backend will be running at http://127.0.0.1:8000

#### 3. Setup and Run Frontend

In a new terminal:

```bash
# Navigate to the app directory
cd src/app

# Install dependencies (first time only)
bun install

# Start the development server
bun run dev
```

The frontend will be running at http://localhost:5173

### Stopping Local Development

```bash
# Stop the backend and frontend with Ctrl+C in their terminals

# Stop the database
docker compose down
```

For more detailed development instructions, see [CONTRIBUTING.md](CONTRIBUTING.md)

## Upcoming Features & Challenges

We use Github's issues feature to track all progress towards any new features or challenges. [Feel free to take a look](https://github.com/Wolfinbarger/game-recommender/issues)!

## Team Members

- Nick Quinn
  - [Github](https://github.com/FreakyNobleGas)
  - [LinkedIn](https://www.linkedin.com/in/nicholas-quinn/)

- X'Zaiver Wolfinbarger
  - [Github](https://github.com/Wolfinbarger)
  - [LinkedIn](https://www.linkedin.com/in/xwolfinbarger/)

* Aaron Harbin
  - [Github](https://github.com/ASHR95)
  - [LinkedIn](https://www.linkedin.com/in/aaron-harbin-ab119b103/)

## License

WIP - [Issue #30](https://github.com/Wolfinbarger/game-recommender/issues/30)

