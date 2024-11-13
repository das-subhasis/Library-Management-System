from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class LibrarianCreate(BaseModel):
    name: str = Field(None, max_length=100)
    password: str
    institution_id: int
    date_of_joining: date
    library_card_id: int

    class Config:
        orm_mode = True

class LibrarianSearch(BaseModel):
    uid: Optional[int] = None
    name: Optional[str] = None
    password: Optional[str] = None
    institution_id: Optional[int] = None

class LibrarianCreateResponse(LibrarianCreate):
    uid: int
    token: str
    expiry_time: int

    class Config:
        orm_mode = True


class MemberCreate(BaseModel):
    name: str = Field(None, max_length=100)
    password: str
    date_of_membership: date
    library_card_id: int
    outstanding_fees: Optional[float] = 0.0
    borrowing_limit: Optional[int] = 10

    class Config:
        orm_mode = True


class MemberResponse(MemberCreate):
    uid: int
    token: str
    expiry_time: int
    class Config:
        orm_mode = True
