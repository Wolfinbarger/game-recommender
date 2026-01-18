"""
Database Connection Manager

This module handles database connections for both local and Docker environments.
It uses SQLModel (which combines SQLAlchemy and Pydantic) to interact with PostgreSQL.

Environment Variables:
- DATABASE_URL: Full connection string (used in Docker)
- USER, PASSWORD: Individual credentials (used in local development)
"""

from sqlmodel import create_engine, Session
from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
# This is important for local development
load_dotenv("../../.env")


class Database:
    """
    Database connection manager.

    This class creates and manages database connections for the application.
    It supports two modes:
    1. Docker: Uses DATABASE_URL environment variable
    2. Local: Constructs URL from USER and PASSWORD environment variables
    """

    def __init__(self):
        # Check if DATABASE_URL is provided (Docker environment)
        # This takes priority over individual credentials
        if "DATABASE_URL" in environ:
            # Docker: Use the full connection string from compose.yaml
            # Format: postgresql://user:password@host:port/database
            self.db_url = environ["DATABASE_URL"]
        else:
            # Local development: Build connection string from individual parts
            self.host = "localhost"
            self.name = "game-recommender"
            self.user = environ.get("USER", "postgres")

            # Password is optional for local development
            self.password = environ.get("PASSWORD", "")

            # Construct the database URL
            self.db_url = self.create_database_url()

    def create_session(self):
        """
        Creates a new database session.

        A session is used to query and modify the database.
        Always use this with a context manager (with statement):
            with db.create_session() as session:
                # Your database operations here

        Returns:
            Session: A SQLModel session object
        """
        engine = create_engine(self.db_url)
        return Session(engine)

    def create_database_url(self) -> str:
        """
        Constructs a PostgreSQL connection URL from individual components.

        Format: postgresql://username:password@hostname/database_name

        Returns:
            str: The database connection URL
        """
        return f"postgresql://{self.user}:{self.password}@{self.host}/{self.name}"

