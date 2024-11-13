from datetime import date
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Depends, HTTPException
from database.database import Settings
from contextlib import asynccontextmanager
from database.database import DB_Session
from pydantic import BaseModel

from models.library import Library


# from models.books import BOOK as BOOK_MODEL

class LibraryBase(BaseModel):
    institution_id: int
    date_of_establishment: date
    institution_name: str
    location: Optional[str] = None

    class Config:
        orm_mode = True


class Book(BaseModel):
    ISBN: int
    title: str
    author: str
    publisher: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Settings.initialize_db()
    yield


app = FastAPI(debug=True, lifespan=lifespan)


@app.get('/v1/')
def home():
    return {'message': 'Welcome to my Library Management API (ver. 1.0)'}


@app.get('/v1/library')
async def get_all_libraries(db: DB_Session):
    res = await db.scalars(select(Library))
    library_data = res.all()
    return library_data


@app.post('/v1/admin/library')
async def create_library(library: LibraryBase, db: DB_Session):
    if not library:
        raise HTTPException(status_code=400, detail="Unable to process data.")
    new_lib = Library(**library.dict())
    db.add(new_lib)
    await db.commit()
    return library
