from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ListingCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., gt=0)
    seller_id: int = Field(..., gt=0)
    category: Optional[str] = Field(None, max_length=100)


class ListingRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    seller_id: int
    category: Optional[str] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
