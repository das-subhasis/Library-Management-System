from sqlalchemy import Column, String, INTEGER, BigInteger, Enum, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT

from Backend.api.v1.db import Settings
from typing import Optional
from enum import Enum as PyEnum

from sqlalchemy.orm import relationship

BASE = Settings.BASE


class Status(PyEnum):
    CHECKED_OUT: str = "checked_out"
    AVAILABLE: str = "available"
    MISSING: str = "missing"
    RESERVED: str = "reserved"


class Book(BASE):
    __tablename__ = "books"
    ISBN: int = Column(BIGINT, primary_key=True)
    title: Optional[str] = Column(String(100))
    author: Optional[str] = Column(String(100))
    publisher: Optional[str] = Column(String(100))

    book_item = relationship("BookItem", back_populates="book")


class BookItem(BASE):
    __tablename__ = "book_items"
    barcode: int = Column(BIGINT, primary_key=True)
    ISBN: int = Column(BIGINT, ForeignKey("books.ISBN", ondelete="CASCADE"))
    status: str = Column(Enum(Status), default=Status.AVAILABLE, nullable=False)
    shelf_id: int = Column(BIGINT, ForeignKey("shelf.shelf_id", ondelete='CASCADE'))
    institution_id: int = Column(BIGINT, ForeignKey("libraries.institution_id", ondelete='CASCADE'))

    book = relationship("Book", back_populates="book_item")
    shelves = relationship("Shelf", back_populates="book_items")
    library = relationship("Library", back_populates="book_items")
    borrowed = relationship("Borrowed", back_populates="book_item")
