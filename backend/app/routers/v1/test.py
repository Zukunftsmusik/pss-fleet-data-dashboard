from fastapi import APIRouter


router = APIRouter(prefix="/test", tags=["test"])


@router.get("/")
async def test_api_route():
    """Use this to verify that CapRover securely forwards /api traffic."""
    return {
        "status": "online",
        "message": "Greetings from the backend! Nginx routing is working perfectly.",
        "container_environment": "CapRover Production Stack",
    }


__all__ = [
    "router",
]
