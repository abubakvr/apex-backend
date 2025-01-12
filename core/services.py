from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import Depends
from api.schemas import Item, ItemCreate
from database.database import get_db

async def get_items():
    items = [
        Item(name="Foo", description="A very nice Foo", price=50.2, tax=2.5),
        Item(name="Bar", price=100.5),
        Item(name="Baz", description="Another item", price=25.0, tax=1.25),
    ]
    return items

async def create_item(
    item: ItemCreate,
    db: AsyncIOMotorDatabase = Depends(get_db)
) -> Item:
    # Convert the Pydantic model to a dictionary
    item_dict = item.model_dump()
    
    # Insert the document into MongoDB
    result = await db.items.insert_one(item_dict)
    
    # Fetch the created document to return it
    created_item = await db.items.find_one({"_id": result.inserted_id})
    
    # Convert MongoDB's _id to string and return as Pydantic model
    created_item["id"] = str(created_item.pop("_id"))
    return Item(**created_item)