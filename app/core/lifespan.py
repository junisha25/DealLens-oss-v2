from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application startup and shutdown events.
    """

    print("=" * 50)
    print(f"Starting {settings.app_name}")
    print(f"Debug Mode: {settings.debug}")
    print("=" * 50)

    yield

    print("=" * 50)
    print(f"Shutting down {settings.app_name}")
    print("=" * 50)