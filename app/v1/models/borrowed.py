from pydantic import BaseModel
from sqlalchemy import Column, String, BIGINT, Enum, DATE, INTEGER, FLOAT, ForeignKey
from database.database import Settings
from typing import Optional, Union
from enum import Enum as PyEnum
from datetime import date

from sqlalchemy.orm import relationship

BASE = Settings.BASE


class SubmissionStatus(PyEnum):
    RETURNED: str = "returned"
    NOT_SUBMITTED: str = "not submitted"
    PAST_DUE: str = "past due"


class Borrowed(BASE):
    __tablename__ = "borrowed"
    instance_id: int = Column(BIGINT, primary_key=True)
    member_id: int = Column(BIGINT, ForeignKey("members.uid", ondelete="CASCADE"))
    barcode_id: int = Column(BIGINT, ForeignKey("book_items.barcode", ondelete="CASCADE"))
    date_of_issue: date = Column(DATE, nullable=False)
    date_of_submission: date = Column(DATE, nullable=False)
    status: str = Column(Enum(SubmissionStatus), default=SubmissionStatus.NOT_SUBMITTED)

    members = relationship("Member", back_populates="borrowed")
    book_item = relationship("BookItem", back_populates="borrowed")
