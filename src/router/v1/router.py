from fastapi import APIRouter
from router.v1.users import user


router = APIRouter(prefix="/v1")
router.include_router(user.router)
