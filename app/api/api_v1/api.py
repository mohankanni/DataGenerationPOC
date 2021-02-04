from fastapi import APIRouter

from .endpoints import revenue

router = APIRouter()
router.include_router(revenue.router, prefix="/revenue", tags=["revenue"])
