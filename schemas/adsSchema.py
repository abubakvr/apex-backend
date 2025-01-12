from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Dict
    
class Side(str, Enum):
    BUY = "0"
    SELL = "1"

class PriceType(str, Enum):
    FIXED = "0"
    FLOATING = "1"

class ItemType(str, Enum):
    ORIGIN = "ORIGIN"
    BULK = "BULK"
    

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
    