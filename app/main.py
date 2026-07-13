from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="DealLens OSS API",
    description="AI-powered SEC Filing Intelligence Platform",
    version="2.0.0",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to DealLens OSS v2 🚀",
    }