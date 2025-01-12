from pydantic import BaseModel, Field
from typing import Optional
from enum import IntEnum

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

class PaymentType(IntEnum):
    """Payment type enumeration - extend with actual values"""
    BANK_TRANSFER = 1
    ALIPAY = 2
    WECHAT = 3
    # Add other payment types as needed

class PaymentMethod(BaseModel):
    """Schema for user payment method information"""
    id: str = Field(
        description="user payment id"
    )
    realName: str = Field(
        description="user real name"
    )
    paymentType: PaymentType = Field(
        description="payment type"
    )
    bankname: Optional[str] = Field(
        None,
        description="Corresponding Bank Name"
    )
    branch_name: Optional[str] = Field(
        None,
        description="Corresponding Branch Name"
    )
    account_no: Optional[str] = Field(
        None,
        description="Account Number"
    )
    qrcode: Optional[str] = Field(
        None,
        description="QR Code Image URL"
    )
    online: str = Field(
        description="Non-Balance Coin Purchase (0 Offline), Balance Coin Purchase (1 Online)"
    )
