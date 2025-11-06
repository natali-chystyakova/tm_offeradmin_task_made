from pydantic import BaseModel
from typing import Optional, List
import uuid

class OfferOut(BaseModel):
    uuid: uuid.UUID
    id: int
    url: Optional[str]
    is_active: bool
    name: str
    sum_to: Optional[str]
    term_to: Optional[int]
    percent_rate: Optional[int]

    class Config:
        orm_mode = True

class OfferAssignmentOut(BaseModel):
    offer: OfferOut

class OfferWallOut(BaseModel):
    token: uuid.UUID
    name: Optional[str]
    url: Optional[str]
    description: Optional[str]
    offer_assignments: List[OfferAssignmentOut]

    class Config:
        orm_mode = True
