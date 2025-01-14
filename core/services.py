from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import Depends
from api.schemas import Item, ItemCreate, Side, PriceType, ItemType
from schemas import orderSchema
from database.database import get_db
from core.bybitClient import HTTP_Request
from typing import List
import json

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

async def get_current_balance():
    endpoint="/v5/asset/transfer/query-account-coins-balance?accountType=FUND&coin=USDT"
    method="GET"
    params=''
    return HTTP_Request(endpoint,method,params,"User Balance")
    
async def get_account_info():
    endpoint="/v5/p2p/user/personal/info"
    method="POST"
    params=''
    response = HTTP_Request(endpoint, method, params, "User Info")  # Capture the return value
    return response 
    
async def get_ads_list():
    endpoint="/v5/p2p/item/personal/list"
    method="POST"
    params=''
    return HTTP_Request(endpoint,method,params,"User Info ")
    
async def get_ad_detail(ad_id: str):
    endpoint = "/v5/p2p/item/info"
    method = "POST"
    params = f'{{"itemId": "{ad_id}"}}'  # Properly formatted JSON string
    return HTTP_Request(endpoint, method, params, "Ad Detail")

async def offline_ads(item_id: str):
    endpoint = "/v5/p2p/item/cancel"
    method = "POST"
    params = f'{{"itemId": "{item_id}"}}'
    return HTTP_Request(endpoint, method, params, "Offline Ads")

async def get_orders(
    params: orderSchema.OrderSearchParams
):
    """
    Get P2P orders with optional filters
    Args:
        page (int): Page number to query
        size (int): Rows to query per page
        status (OrderStatus, optional): Order status filter
        begin_time (str, optional): Begin time filter
        end_time (str, optional): End time filter
        token_id (str, optional): Token ID filter
        sides (List[int], optional): List of sides to filter by
    """
    endpoint = "/v5/p2p/order/simplifyList"
    method = "POST"
    formatted_params = json.dumps(params.model_dump())
    return HTTP_Request(endpoint, method, formatted_params, "Get Orders")
    
async def get_pending_orders():
    """
    Get all pending P2P orders
    """
    endpoint = "/v5/p2p/order/pending/simplifyList"
    method = "POST"
    params = ''  # Empty string as no parameters are required
    return HTTP_Request(endpoint, method, params, "Get Pending Orders")
    
async def get_user_order_stats(original_uid: str, order_id: str):
    """
    Get user's order statistics
    Args:
        original_uid (str): Counterparty user ID
        order_id (str): Order ID
    """
    endpoint = "/v5/p2p/user/order/personal/info"
    method = "POST"
    params = json.dumps({
        "originalUid": str(original_uid),
        "orderId": str(order_id)
    })
    
    print(original_uid)
    
    return HTTP_Request(endpoint, method, params, "Get User Order Stats")
    
async def get_order_details(order_id: str):
    """
    Get detailed information for a specific P2P order
    Args:
        order_id (str): The ID of the order to retrieve details for
    """
    endpoint = "/v5/p2p/order/info"
    method = "POST"
    params = json.dumps({
        "orderId": order_id
    })
    return HTTP_Request(endpoint, method, params, "Get Order Details")

async def release_digital_asset(order_id: str):
    """
    Release digital assets for a P2P order
    Args:
        order_id (str): The ID of the order to release assets for
    """
    endpoint = "/v5/p2p/order/finish"
    method = "POST"
    params = json.dumps({
        "orderId": order_id
    })
    return HTTP_Request(endpoint, method, params, "Release Digital Asset")
    
async def mark_order_as_paid(order_id: str, payment_type: str, payment_id: str):
    """
    Mark a P2P order as paid
    Args:
        order_id (str): The ID of the order being paid
        payment_type (str): Payment method used (from order detail interface)
        payment_id (str): Payment method ID used (from order detail interface)
    """
    endpoint = "/v5/p2p/order/pay"
    method = "POST"
    params = json.dumps({
        "orderId": order_id,
        "paymentType": payment_type,
        "paymentId": payment_id
    })
    return HTTP_Request(endpoint, method, params, "Mark Order As Paid")
    
async def create_p2p_ad(
    token_id: str,
    currency_id: str,
    side: Side,
    price_type: PriceType,
    premium: str,
    price: str,
    min_amount: str,
    max_amount: str,
    remark: str,
    trading_preference_set: dict,
    payment_ids: List[str],
    quantity: str,
    payment_period: str,
    item_type: ItemType = ItemType.ORIGIN
):
    """
    Create a new P2P advertisement
    Args:
        token_id (str): Token ID
        currency_id (str): Currency ID
        side (Side): BUY or SELL
        price_type (PriceType): FIXED or FLOATING rate
        premium (str): Floating ratio with current exchange rate
        price (str): Advertisement price
        min_amount (str): Minimum transaction amount
        max_amount (str): Maximum transaction amount
        remark (str): Transaction description (max 900 chars)
        trading_preference_set (dict): Trading preferences object
        payment_ids (List[str]): List of payment method type IDs (max 5)
        quantity (str): Number of advertisements
        payment_period (str): Payment duration
        item_type (ItemType): ORIGIN or BULK advertisement type
    """
    if len(payment_ids) > 5:
        raise ValueError("Maximum 5 payment methods allowed")
    
    if len(remark) > 900:
        raise ValueError("Remark must not exceed 900 characters")

    endpoint = "/v5/p2p/item/create"
    method = "POST"
    params = json.dumps({
        "tokenId": token_id,
        "currencyId": currency_id,
        "side": side.value,
        "priceType": price_type.value,
        "premium": premium,
        "price": price,
        "minAmount": min_amount,
        "maxAmount": max_amount,
        "remark": remark,
        "tradingPreferenceSet": trading_preference_set,
        "paymentIds": payment_ids,
        "quantity": quantity,
        "paymentPeriod": payment_period,
        "itemType": item_type.value
    })
    return HTTP_Request(endpoint, method, params, "Create P2P Ad")
    
async def get_online_ads(
    token_id: str,
    currency_id: str,
    side: Side,
    page: str = "1",
    size: str = "10"
):
    """
    Get list of online P2P advertisements
    Args:
        token_id (str): Token ID (e.g., USDT, ETH, BTC)
        currency_id (str): Currency ID (e.g., HKD, USD, EUR)
        side (Side): BUY or SELL (0 or 1)
        page (str, optional): Page number (default: "1")
        size (str, optional): Page size (default: "10")
    """
    endpoint = "/v5/p2p/item/online"
    method = "POST"
    params = json.dumps({
        "tokenId": token_id,
        "currencyId": currency_id,
        "side": side.value,
        "page": page,
        "size": size
    })
    return HTTP_Request(endpoint, method, params, "Get Online Ads")
    
async def get_user_payments():
    """
    Get list of user's payment methods
    Returns all payment methods associated with the authenticated user
    """
    endpoint = "/v5/p2p/user/payment/list"
    method = "POST"
    params = ''  # Empty string as no parameters are required
    response =  HTTP_Request(endpoint, method, params, "Get User Payments")
    return response