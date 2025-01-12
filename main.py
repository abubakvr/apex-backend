from fastapi import FastAPI
from api.endpoints import router
from config.settings import settings
from database.database import connect_to_mongodb, close_mongodb_connection

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
app.include_router(router)

async def startup():
    await connect_to_mongodb()

async def shutdown():
    await close_mongodb_connection()