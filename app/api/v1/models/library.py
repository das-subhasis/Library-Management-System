from pydantic import BaseModel
from sqlalchemy import Column, String, INTEGER, BIGINT, ForeignKey, DATE, Enum
from app.api.v1.db import Settings
from typing import Optional, Union
from datetime import date
from enum import Enum as PyEnum

from sqlalchemy.orm import relationship

BASE = Settings.BASE


class CardStatus(PyEnum):
    VALID: str = "valid"
    INVALID: str = "invalid"
    EXPIRED: str = "expired"


class Library(BASE):
    __tablename__ = "libraries"
    institution_id: int = Column(BIGINT, primary_key=True)
    date_of_establishment: date = Column(DATE, nullable=False)
    institution_name: Union[str, None] = Column(String(100), nullable=False, unique=True)
    location: Union[str, None] = Column(String(120), nullable=True)

    shelves = relationship("Shelf", back_populates="library")
    book_items = relationship("BookItem", back_populates="library")


class Shelf(BASE):
    __tablename__ = "shelf"
    shelf_id: int = Column(BIGINT, primary_key=True)
    institution_id: int = Column(BIGINT, ForeignKey('libraries.institution_id', ondelete='CASCADE'))
    subject: str = Column(String(100), nullable=True, server_default='NA')

    library = relationship("Library", back_populates="shelves")
    book_items = relationship("BookItem", back_populates="shelves")


class LibraryCard(BASE):
    __tablename__ = "library_card"
    library_card_id: int = Column(BIGINT, primary_key=True)
    barcode: int = Column(BIGINT, nullable=False, unique=True)
    issue_date: date = Column(DATE, nullable=False)
    date_of_expiration: date = Column(DATE, nullable=False)
    status: str = Column(Enum(CardStatus), default=CardStatus.VALID)

