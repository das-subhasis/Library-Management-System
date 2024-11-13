from fastapi import HTTPException, status
from sqlalchemy import select, and_
from Backend.api.v1.models import Librarian
from Backend.api.v1.schemas import LibrarianCreate, LibrarianSearch
from Backend.api.v1.db import DB_Session


async def create_librarian_account(db: DB_Session, librarian_data: LibrarianCreate):
    exists = await db.scalars(select(Librarian).where(
        and_(Librarian.name == librarian_data.name,
             Librarian.password == librarian_data.password
             )))

    if exists.all():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists.")

    new_librarian = Librarian(**librarian_data.model_dump())
    db.add(new_librarian)
    await db.commit()
    await db.refresh(new_librarian)
    return new_librarian


async def search_all_librarian(db: DB_Session):
    res = await db.scalars(select(Librarian))
    return res.all()


async def search_librarian_by_name_and_password(db: DB_Session, library: LibrarianSearch):
    res = await db.scalars(select(Librarian).where(
        and_(Librarian.name == library.name,
             Librarian.password == library.password
             )))
    return res.first()


async def search_librarian_by_id(db: DB_Session, uid: int):
    res = await db.scalars(select(Librarian).where(Librarian.uid == uid))
    return res.all()


async def search_librarian_by_institution_id(db: DB_Session, institution_id: int):
    res = await db.scalars(select(Librarian).where(Librarian.institution_id == institution_id))
    return res.all()


async def search_librarian_by_name(db: DB_Session, name: str):
    res = await db.scalars(select(Librarian).where(Librarian.name == name))
    return res.all()


async def remove_librarian(db: DB_Session, library: LibrarianSearch):
    res = await db.scalars(select(Librarian).where(
        and_(Librarian.name == library.name,
             Librarian.password == library.password
             )))
    lib = res.first()
    db.delete(lib)
    await db.commit()
    return lib
