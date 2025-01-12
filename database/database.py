from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config import settings  # Assuming settings.py contains your MongoDB connection string

client = None
db = None
async def connect_to_mongodb():
    global client
    try:
        client = AsyncIOMotorClient(settings.MONGODB_URI)
        db = client.bybitdb
        print("Connected to MongoDB")
        # Optionally test the connection:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise  # Re-raise the exception to halt startup if connection fails

async def close_mongodb_connection():
    global client
    if client:
        client.close()
        print("Closed MongoDB connection")
        
async def get_db() -> AsyncIOMotorDatabase:
    return db