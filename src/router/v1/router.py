from fastapi import APIRouter
from router.v1.users import user
from router.v1.authentication import authentication
from router.v1.stations import station
from router.v1.stations import route
from router.v1.trains import train
from router.v1.wagons import wagon

router = APIRouter(prefix="/v1")
router.include_router(authentication.router, tags=["Аутентификация"], prefix="/auth")
router.include_router(user.router, tags=["Пользователи"], prefix="/user")
router.include_router(station.router, tags=["Станции"], prefix="/stations")
router.include_router(route.router, tags=["Маршруты"], prefix="/routes")
router.include_router(train.router, tags=["Поезда"], prefix="/trains")
router.include_router(wagon.router, tags=["Вагоны"], prefix="/wagons")
