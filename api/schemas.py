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
    
class UserProfile(BaseModel):
    nickName: str = Field(description="User's nickname")
    defaultNickName: bool = Field(
        description="Whether the user's nickname is system-generated. true: system-generated, false: user-set"
    )
    isOnline: bool = Field(
        description="Whether the user is online on the bybit site. true: online, false: offline"
    )
    kycLevel: str = Field(description="KYC level")
    email: str = Field(description="Email address (masked)")
    mobile: str = Field(description="Mobile phone number (masked)")
    lastLogoutTime: str = Field(description="Last logout time from bybit platform")
    recentRate: str = Field(description="Completion rate in the past 30 days")
    totalFinishCount: int = Field(description="Total number of completed orders")
    totalFinishSellCount: int = Field(
        description="Total number of completed orders - sell token"
    )
    totalFinishBuyCount: int = Field(
        description="Total number of completed orders - buy token"
    )
    recentFinishCount: int = Field(description="Order quantity within 30 days")
    averageReleaseTime: str = Field(
        description="Average release token time in minutes"
    )
    averageTransferTime: str = Field(
        description="Average payment currency time in minutes"
    )
    accountCreateDays: int = Field(description="Days since the account was created")
    firstTradeDays: int = Field(
        description="Days from first transaction to today"
    )
    realName: str = Field(description="Real name")
    recentTradeAmount: str = Field(
        description="Cumulative successful transaction amount USDT in the past 30 days"
    )
    totalTradeAmount: str = Field(
        description="The sum of all USDT transaction volumes in the past for the account"
    )
    registerTime: str = Field(description="User's registration time")
    authStatus: int = Field(
        description="VA status: 1 - VA, 2 - Not VA"
    )
    kycCountryCode: str = Field(description="User's KYC country code")
    blocked: str = Field(description="User's banned status")
    goodAppraiseRate: str = Field(description="Positive rating")
    goodAppraiseCount: int = Field(description="Number of positive comments")
    badAppraiseCount: int = Field(description="Number of negative comments")
    vipLevel: int = Field(description="VIP level")
    userId: str = Field(description="UserId")
    realNameEn: Optional[str] = Field(
        description="KYC in English",
        default=None
    )
