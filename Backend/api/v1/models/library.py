from sqlalchemy import Column, String, BIGINT, ForeignKey, DATE, Enum
from enum import Enum as PyEnum
from Backend.api.v1.db import Settings
from Backend.api.v1.core import generate_id

from sqlalchemy.orm import relationship

BASE = Settings.BASE


class CardStatus(PyEnum):
    VALID: str = "valid"
    INVALID: str = "invalid"
    EXPIRED: str = "expired"


class Library(BASE):
    __tablename__ = "libraries"
    institution_id: int = Column(BIGINT, primary_key=True, default=generate_id)
    date_of_establishment: str = Column(DATE, nullable=False)
    institution_name: str = Column(String(100), nullable=False)
    location: str = Column(String(120), nullable=False)

    shelves = relationship("Shelf", back_populates="library")
    book_items = relationship("BookItem", back_populates="library")


class Shelf(BASE):
    __tablename__ = "shelf"
    shelf_id: int = Column(BIGINT, primary_key=True)
    institution_id: int = Column(BIGINT, ForeignKey('libraries.institution_id', ondelete='CASCADE'))
    subject: str = Column(String(100), nullable=True)

    library = relationship("Library", back_populates="shelves")
    book_items = relationship("BookItem", back_populates="shelves")


class LibraryCard(BASE):
    __tablename__ = "library_card"
    librarian_id: int = Column(BIGINT, ForeignKey("librarian.uid"))
    barcode: int = Column(BIGINT, nullable=False, unique=True, primary_key=True)
    issue_date: str = Column(DATE, nullable=False)
    date_of_expiration: str = Column(DATE, nullable=False)
    status: str = Column(Enum(CardStatus), default=CardStatus.VALID)
