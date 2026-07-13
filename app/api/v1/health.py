from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    """
    Health check endpoint.

    Returns the current status of the API.
    """
    return {
        "status": "healthy",
        "service": "DealLens OSS API",
        "version": "2.0.0",
    }