# Python Documentation

## Overview
We are using the FastAPI Python framework to serve API requests from our client and interact
with our PostgreSQL database through SQLModel.

## How to run locally
Note: All the following commands should be executed from the ./src/api directory.

Install required modules: (See dependencies section below for more information)
`pip install --user -r requirements.txt`

Setup PostgreSQL Database (Assumes you already have PostgreSQL installed)
Use the built-in Postgres CLI tool to create the new database
`createdb game-recommender`

Copy the pg service conf file to your home directory.
`cp ./api/.pg_service.conf ~/`

Use the built-in Postgres CLI tool to create a new user.
`createuser --interactive`

Use this as reference for answering the prompts
`
Enter name of role to add: USER
Shall the new role be a superuser? (y/n) y
`

Run DB migration using alembic:
`alembic upgrade head`

Start API server: `fastapi dev main.py`

## Running from Docker container
The API service can be run locally by either building a new image or running a previously built image. If you would
like to build a new image, please see the instructions at the top of the Dockerfile in this directory.

If you just need to run the latest image, do the following:
- Confirm you are in the project's root directory with the .env file.
- Run: `docker run --env-file=.env -p 8000:8000 -p 5432:5432 freakynoblegas/game-recommender:api-latest`

## Testing Locally
You can confirm that the app is running properly by using this endpoint:
- GET `http://127.0.0.1:8000/api/games`

## Dependencies
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [Psycopg3](https://www.psycopg.org/psycopg3/)