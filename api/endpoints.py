from fastapi import APIRouter, Depends
from core.services import get_items, create_item
from api.schemas import Item, ItemCreate

router = APIRouter(prefix="/api")

@router.get("/")
async def read_items(items: list[Item] = Depends(get_items)):
    return items

@router.post("/", response_model=Item)
async def create_item_endpoint(item: ItemCreate = Depends(create_item)):
    return item