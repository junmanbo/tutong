from pydantic import BaseModel
from typing import Optional

# Shared properties
class TickerBase(BaseModel):
    exchange_id: Optional[int] = None
    asset_type_id: Optional[int] = None
    symbol: Optional[str] = None
    currency: Optional[str] = None
    ticker_knm: Optional[str] = None
    marketcap: Optional[int] = None
    maker_fee: Optional[float] = None
    taker_fee: Optional[float] = None

# Properties to receive via API on creation
class TickerCreate(TickerBase):
    exchange_id: int
    asset_type_id: int
    symbol: str
    currency: str

# Properties to receive via API on update
class TickerUpdate(TickerBase):
    pass

class TickerInDBBase(TickerBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
class Ticker(TickerInDBBase):
    pass

# Additional properties stored in DB
class TickerInDB(TickerInDBBase):
    pass

