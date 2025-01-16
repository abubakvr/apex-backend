from fastapi import FastAPI
from api.endpoints import router
from config.settings import settings
from database.database import connect_to_mongodb, close_mongodb_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods including OPTIONS
    allow_headers=["*"],
)

async def startup():
    await connect_to_mongodb()

async def shutdown():
    await close_mongodb_connection()