from pydantic import BaseModel, Field
from typing import Union, Optional

class LibraryCreate(BaseModel):
    institution_name: str = Field(..., max_length=100)
    date_of_establishment: str
    location: Optional[str] = None

    class Config:
        orm_mode = True
