from pydantic import BaseModel, Field
from enum import IntEnum, Enum
from typing import List, Optional, Dict

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
class OrderStatus(IntEnum):
    WAITING_FOR_CHAIN = 5
    WAITING_FOR_BUY_PAY = 10
    WAITING_FOR_SELLER_RELEASE = 20
    APPEALING = 30
    CANCEL_ORDER = 40
    FINISH_ORDER = 50
    PAYING = 60
    PAY_FAIL = 70
    EXCEPTION_CANCELED = 80
    WAITING_BUYER_SELECT_TOKEN = 90
    OBJECTING = 100
    WAITING_FOR_OBJECTION = 110
    
class Side(str, Enum):
    BUY = "0"
    SELL = "1"

class PriceType(str, Enum):
    FIXED = "0"
    FLOATING = "1"

class ItemType(str, Enum):
    ORIGIN = "ORIGIN"
    BULK = "BULK"
    
class OrderType(str):
    ORIGIN = "ORIGIN"
    SMALL_COIN = "SMALL_COIN"
    WEB3 = "WEB3"

class UserType(str):
    PERSONAL = "PERSONAL"
    ORG = "ORG"
    
class P2PAdCreate(BaseModel):
    token_id: str
    currency_id: str
    side: Side
    price_type: PriceType
    premium: str
    price: str
    min_amount: str
    max_amount: str
    remark: str
    trading_preference_set: Dict
    payment_ids: List[str]
    quantity: str
    payment_period: str
    item_type: ItemType = ItemType.ORIGIN
