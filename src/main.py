import uvicorn
import settings
from fastapi import FastAPI

from router.api import api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.HOST, port=settings.PORT)
