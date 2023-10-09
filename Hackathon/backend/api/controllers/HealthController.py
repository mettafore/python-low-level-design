"""Health check controller."""
from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=["Health"])


@health_router.get("")
async def health_check():
    """Check status of application."""
    return {"status": "ok"}
