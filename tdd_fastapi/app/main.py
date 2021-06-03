from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from .config import get_settings, Settings

app = FastAPI()


register_tortoise(
    app,
    db_url=get_settings().database_url,
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
            "ping": "pong!",
            "environment": settings.environment,
            "testing": settings.testing
        }