from fastapi import APIRouter
from router.v1.users import user
from router.v1.authentication import authentication
from router.v1.stations import station

router = APIRouter(prefix="/v1")
router.include_router(authentication.router, tags=["Аутентификация"], prefix="/auth")
router.include_router(user.router, tags=["Пользователи"], prefix="/user")
router.include_router(station.router, tags=["Станции"], prefix="/stations")
