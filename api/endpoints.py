from fastapi import APIRouter, Depends
from core import services
from api.schemas import Item, ItemCreate, Side
from schemas import orderSchema, userSchema, adsSchema

router = APIRouter(prefix="/api")

@router.get("/")
async def read_items(items: list[Item] = Depends(services.get_items)):
    return items

@router.post("/", response_model=Item)
async def create_item_endpoint(item: ItemCreate = Depends(services.create_item)):
    return item

@router.get("/account")  # New endpoint
async def read_account_info():
    return await services.get_account_info()

@router.get("/ads/my")
async def list_my_ads():
    """Get list of personal P2P advertisements"""
    return await services.get_ads_list()

@router.get("/ads/{ad_id}")
async def get_ad_detail(ad_id: str):
    """Get details of a specific P2P advertisement"""
    return await services.get_ad_detail(ad_id)

@router.post("/ads/create")
async def create_ad(ad_data: adsSchema.P2PAdCreate):
    """Create a new P2P advertisement"""
    return await services.create_p2p_ad(**ad_data.model_dump())

@router.delete("/ads/offline/{item_id}")
async def take_ad_offline(item_id: str):
    """Take a P2P advertisement offline"""
    return await services.offline_ads(item_id)

@router.get("/ads/online")
async def get_online_advertisements(
    token_id: str,
    currency_id: str,
    side: Side,
    page: str = "1",
    size: str = "10"
):
    """Get list of online P2P advertisements"""
    return await services.get_online_ads(token_id, currency_id, side, page, size)

@router.post("/orders")
async def get_orders_list(
    params: orderSchema.OrderSearchParams
):
    """Get filtered list of P2P orders"""
    return await services.get_orders(params)

@router.get("/orders/pending")
async def get_pending_orders_list():
    """Get list of pending P2P orders"""
    return await services.get_pending_orders()

@router.get("/orders/{order_id}")
async def get_order_details(order_id: str):
    """Get detailed information for a specific order"""
    return await services.get_order_details(order_id)

@router.post("/orders/{order_id}/pay")
async def mark_paid(
    order_id: str,
    payment_type: str,
    payment_id: str
):
    """Mark a P2P order as paid"""
    return await services.mark_order_as_paid(order_id, payment_type, payment_id)

@router.get("/orders/{order_id}/stats", response_model=userSchema.UserProfile)
async def get_order_stats(order_id: str, original_uid: str):
    """Get statistics for a specific order"""
    return await services.get_user_order_stats(original_uid, order_id)

@router.post("/orders/{order_id}/release")
async def release_asset(order_id: str):
    """Release digital assets for a P2P order"""
    return await services.release_digital_asset(order_id)

@router.get("/payments")
async def get_payment_methods():
    """Get list of user's payment methods"""
    return await services.get_user_payments()



