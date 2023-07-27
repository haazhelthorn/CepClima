from functools import lru_cache

import uvicorn as uvicorn
from fastapi import FastAPI, Depends

from routers import api_cep
from schema.settings import Settings

app = FastAPI()
app.include_router(api_cep.router, prefix="/v1", tags=["v1"])


@lru_cache()
def get_settings():
    return Settings()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "idapi": settings.idapi
    }


@app.get("/")
async def root():
    return {"message": "Sou uma api"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
