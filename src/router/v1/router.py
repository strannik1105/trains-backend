from fastapi import APIRouter
from router.v1.users import user
from router.v1.authentication import authentication

router = APIRouter(prefix="/v1")
router.include_router(authentication.router, tags=["Аутентификация"], prefix="/auth")
router.include_router(user.router, tags=["Пользователи"], prefix="/user")
