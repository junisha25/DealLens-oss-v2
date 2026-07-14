from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.lifespan import lifespan


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )

    app.include_router(api_router)

    @app.get("/", tags=["Root"])
    def root():
        return {
            "message": f"Welcome to {settings.app_name} 🚀",
            "debug": settings.debug,
        }

    return app


app = create_app()