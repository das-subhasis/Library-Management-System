from pydantic import BaseModel
from sqlalchemy import Column, String, BIGINT, Enum, DATE, INTEGER, FLOAT, ForeignKey
from database.database import Settings
from typing import Optional, Union
from enum import Enum as PyEnum
from datetime import date

from sqlalchemy.orm import relationship

BASE = Settings.BASE


class Librarian(BASE):
    __tablename__ = "librarian"
    uid: int = Column(BIGINT, primary_key=True)
    name: Optional[str] = Column(String(100))
    password: str = Column(String(150))
    institution_id: int = Column(BIGINT, ForeignKey("libraries.institution_id", ondelete="CASCADE"))
    date_of_joining: date = Column(DATE, nullable=False)
    library_card_id: int = Column(BIGINT, nullable=False)


class Member(BASE):
    __tablename__ = "members"
    uid: int = Column(BIGINT, primary_key=True)
    name: Optional[str] = Column(String(100))
    password: str = Column(String(150))
    date_of_membership: date = Column(DATE, nullable=False)
    library_card_id: int = Column(BIGINT, nullable=False)
    outstanding_fees: float = Column(FLOAT, default=0.0)
    borrowing_limit: int = Column(INTEGER, default=10)
    total_books_borrowed: int = Column(INTEGER, default=0)

    borrowed = relationship("Borrowed", back_populates="members")
