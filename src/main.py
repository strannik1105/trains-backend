import uvicorn
from fastapi_jwt_auth import AuthJWT

import settings
from fastapi import FastAPI

from router.api import api_router

app = FastAPI()
app.include_router(api_router)


@AuthJWT.load_config
def get_config():
    return settings.cookies_settings


if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.HOST, port=settings.PORT)
