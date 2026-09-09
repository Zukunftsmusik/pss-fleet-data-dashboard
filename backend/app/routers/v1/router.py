from fastapi import APIRouter

from . import players, test


router = APIRouter(prefix="/v1")

router.include_router(players.router)
router.include_router(test.router)

__all__ = [
    "router",
]
