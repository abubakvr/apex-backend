from pydantic import BaseModel, Field
from enum import IntEnum, Enum
from typing import List, Optional
    
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

class OrderType(str):
    ORIGIN = "ORIGIN"
    SMALL_COIN = "SMALL_COIN"
    WEB3 = "WEB3"

class UserType(str):
    PERSONAL = "PERSONAL"
    ORG = "ORG"

    
class OtcPaymentTerm(BaseModel):
    id: str = Field(description="payment id")
    realName: str = Field(description="realname")
    paymentType: int = Field(description="payment type")
    bankName: Optional[str] = Field(None, description="bank name")
    branchName: Optional[str] = Field(None, description="branch name")
    accountNo: Optional[str] = Field(None, description="account no")
    qrcode: Optional[str] = Field(None, description="QR code")
    
class Extension(BaseModel):
    isDelayWithdraw: bool = Field(description="Delayed withdrawal (true: delay)")
    delayTime: str = Field(description="delay time")
    startTime: str = Field(description="delay start time")
    
class OtcOrderInfo(BaseModel):
    model_config = {
        "arbitrary_types_allowed": True
    }
    id: str = Field(description="order id")
    side: int = Field(description="Order trade type. 0: BUY, 1: SELL")
    itemId: str = Field(description="adv id")
    userId: str = Field(description="The uid of the current query user")
    nickName: str = Field(description="The nickname of the current query user")
    makerUserId: str = Field(description="adv owner user")
    targetUserId: str = Field(description="Counterparty uid")
    targetNickName: str = Field(description="Counterparty nickname")
    targetConnectInformation: str = Field(description="Counterparty contact information")
    sellerRealName: str = Field(description="seller realName")
    buyerRealName: str = Field(description="buyer realName")
    tokenId: str = Field(description="token id. e.g. USDT,ETH,BTC")
    currencyId: str = Field(description="currency id . e.g. USD,VND")
    price: str = Field(description="order price")
    quantity: str = Field(description="seller/buyer trade quantity")
    amount: str = Field(description="seller/buyer trade amount")
    paymentType: int = Field(description="Payment method used")
    transferDate: str = Field(description="buyer pay time")
    status: OrderStatus = Field(description="order status")
    createDate: str = Field(description="order create time")
    paymentTermList: List[OtcPaymentTerm] = Field(
        description="Payment method provided by the seller"
    )
    remark: str = Field(description="adv remark info")
    trasferLastSeconds: str = Field(description="The buyer's remaining transfer time")
    appealContent: Optional[str] = Field(None, description="appeal content")
    appealType: Optional[int] = Field(None, description="appeal type")
    appealNickName: Optional[str] = Field(None, description="appeal user nick name")
    canAppeal: str = Field(description="user can appeal")
    confirmedPayTerm: Optional[OtcPaymentTerm] = Field(
        None, description="buyer select payment info"
    )
    makerFee: str = Field(description="maker fee")
    takerFee: str = Field(description="taker fee")
    extension: Extension = Field(description="Order extension information")
    orderType: OrderType = Field(
        description="order type: ORIGIN, SMALL_COIN, or WEB3 p2p order"
    )
    appealUserId: Optional[str] = Field(None, description="appealing uid")
    notifyTokenId: Optional[str] = Field(None, description="buyer revice token")
    notifyTokenQuantity: Optional[str] = Field(
        None, description="buyer revise token quantity"
    )
    cancelReason: Optional[str] = Field(None, description="order cancel reason")
    usedCoupon: bool = Field(description="Whether the order uses a coupon")
    couponTokenId: Optional[str] = Field(None, description="coupon tokenId")
    couponQuantity: Optional[str] = Field(None, description="coupon quantity")
    targetUserType: UserType = Field(
        description="Counterparty Identity Type: PERSONAL or ORG"
    )
    
class OrderItem(BaseModel):
    id: str = Field(description="order Id")
    side: int = Field(description="Order trade type. 0: BUY, 1: SELL")
    tokenId: str = Field(description="tokenId")
    orderType: str = Field(
        description="order type: ORIGIN (Normal p2p order), SMALL_COIN (HotSwap p2p order), WEB3 (web3 p2p order)"
    )
    amount: str = Field(description="seller/buyer trade amount")
    currencyId: str = Field(description="currency_id")
    price: str = Field(description="order price")
    fee: str = Field(description="fee")
    targetNickName: str = Field(description="Counterparty nickname")
    targetUserId: str = Field(description="Counterparty uid")
    status: OrderStatus = Field(description="order status")
    createDate: str = Field(description="order create time")
    transferLastSeconds: str = Field(description="The buyer's remaining transfer time")
    userId: str = Field(description="The uid of the current query user")
    sellerRealName: str = Field(description="seller realname")
    buyerRealName: str = Field(description="buyer realname")
    extension: Extension = Field(description="Order extension information")

class OrderListResponse(BaseModel):
    count: int = Field(description="order total num")
    items: List[OrderItem] = Field(description="list of orders")
    
class OrderStatus(IntEnum):
    """Order status enumeration"""
    WAITING_FOR_CHAIN = 5        # waiting for chain (only web3)
    WAITING_FOR_BUY_PAY = 10     # waiting for buy pay
    WAITING_FOR_SELLER_RELEASE = 20  # waiting for seller release
    APPEALING = 30               # Appealing
    CANCEL_ORDER = 40            # cancel order
    FINISH_ORDER = 50            # finish order
    PAYING = 60                  # paying (only pay online)
    PAY_FAIL = 70               # pay fail (only pay online)
    EXCEPTION_CANCELED = 80      # exception canceled (coin converted to other coin)
    WAITING_BUYER_SELECT_TOKEN = 90  # waiting buyer select tokenId
    OBJECTING = 100             # objectioning
    WAITING_FOR_OBJECTION = 110  # Waiting for the user to raise an objection

class OrderType(str, Enum):
    """Order type enumeration"""
    ORIGIN = "ORIGIN"           # Normal p2p order
    SMALL_COIN = "SMALL_COIN"   # HotSwap p2p order
    WEB3 = "WEB3"              # web3 p2p order

class OrderExtension(BaseModel):
    """Order extension information"""
    isDelayWithdraw: bool = Field(
        description="Delayed withdrawal (true: delay)"
    )
    delayTime: str = Field(
        description="delay time"
    )
    startTime: str = Field(
        description="delay start time"
    )
    
class OrderSearchParams(BaseModel): 
    page: int
    size: int
    status: Optional[OrderStatus] = None
    begin_time: Optional[str] = None
    end_time: Optional[str] = None
    token_id: Optional[str] = None
    side: Optional[int] = None

class OrderItem(BaseModel):
    """Individual order item"""
    id: str = Field(description="order Id")
    side: int = Field(description="Order trade type. 0: BUY, 1: SELL")
    tokenId: str = Field(description="tokenId")
    orderType: OrderType = Field(description="order type")
    amount: str = Field(description="seller/buyer trade amount")
    currencyId: str = Field(description="currency_id")
    price: str = Field(description="order price")
    fee: str = Field(description="fee")
    targetNickName: str = Field(description="Counterparty nickname")
    targetUserId: str = Field(description="Counterparty uid")
    status: OrderStatus = Field(description="order status")
    createDate: str = Field(description="order create time")
    transferLastSeconds: str = Field(description="The buyer's remaining transfer time")
    userId: str = Field(description="The uid of the current query user")
    sellerRealName: str = Field(description="seller realname")
    buyerRealName: str = Field(description="buyer realname")
    extension: OrderExtension = Field(description="Order extension information")

class OrderListResponse(BaseModel):
    """Response model for order list"""
    count: int = Field(description="order total num")
    items: List[OrderItem] = Field(description="list of orders")
    
class OrderPaymentInfo(BaseModel):
    orderId: str = Field(description="order id")
    paymentType: str = Field(description="Payment method used; get from order detail interface")
    paymentId: str = Field(description="Payment method id used; get from order detail interface")