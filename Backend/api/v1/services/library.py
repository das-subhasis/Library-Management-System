from fastapi import Query, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select, and_, or_
from Backend.api.v1.core import generate_batch
from Backend.api.v1.models import Library, Librarian
from Backend.api.v1.schemas import LibraryCreate, LibrarySearch
from Backend.api.v1.db import DB_Session
from typing import List, Optional, Annotated


class FilterQueryParams(BaseModel):
    institution_id: Optional[int] = None
    institution_name: Optional[str] = None
    location: Optional[str] = None


async def search_libraries(db: DB_Session, q: Annotated[FilterQueryParams, Query()]):
    query = select(Library)

    if q.institution_id:
        query = query.filter(Library.institution_id == q.institution_id)
    if q.institution_name:
        query = query.filter(Library.institution_name == q.institution_name)
    if q.location:
        query = query.filter(Library.location == q.location)

    res = await db.scalars(query)
    return res.all()


async def search_all_libraries(db: DB_Session):
    res = await db.scalars(select(Library))
    return res.all()


async def search_library_by_name_and_location(db: DB_Session, library: LibrarySearch):
    res = await db.scalars(select(Library).where(
        and_(Library.institution_name == library.institution_name,
             Library.location == library.location
             )))
    return res.first()


async def search_libraries(db: DB_Session, q: Annotated[FilterQueryParams, Query()]):
    query = select(Library)

    if q.institution_id:
        query = query.filter(Library.institution_id == q.institution_id)
    if q.institution_name:
        query = query.filter(Library.institution_name == q.institution_name)
    if q.location:
        query = query.filter(Library.location == q.location)

    res = await db.scalars(query)
    return res.all()


async def search_library_by_id(db: DB_Session, institution_id: int):
    res = await db.scalars(select(Library).where(Library.institution_id == institution_id))
    return res.all()


async def search_library_by_name(db: DB_Session, institution_name: str):
    res = await db.scalars(select(Library).where(Library.institution_name == institution_name))
    return res.all()


async def search_library_by_location(db: DB_Session, location: str):
    res = await db.scalars(select(Library).where(Library.location == location))
    return res.all()


async def add_library(db: DB_Session, library_data: LibraryCreate):
    try:
        exists = await db.scalars(select(Library).where(
            and_(
                Library.institution_name == library_data.institution_name,
                Library.location == library_data.location
            )))
        if exists.all():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Library already exists"
            )

        new_library = Library(**library_data.model_dump())
        db.add()
        await db.commit()
        await db.refresh(new_library)
        return new_library

    except Exception as e:
        print(e)


async def bulk_add_libraries(db: DB_Session, libraries: List[LibraryCreate]):
    new_libraries = []
    existing_libraries = []
    try:
        for lib_list in generate_batch(libraries):
            for library in lib_list:
                exists = await db.scalars(select(Library).where(
                    and_(
                        Library.institution_name == library.institution_name,
                        Library.location == library.location
                    )))

                if not exists.all():
                    new_library = Library(**library.model_dump())
                    new_libraries.append(new_library)
                else:
                    existing_library = Library(**library.model_dump())
                    existing_libraries.append(existing_library)

            if new_libraries:
                db.add_all(new_libraries)
                await db.commit()
                new_libraries.clear()

        return {'message': 'Data inserted successfully',
                'existing_data': existing_libraries}

    except Exception as e:
        print(e)


async def remove_library(db: DB_Session, library_data: LibrarySearch):
    res = await db.scalars(select(Library).where(
        and_(
            Library.institution_name == library_data.institution_name,
            Library.location == library_data.location
        )))

    library = res.first()

    if not library:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find library"
        )

    await db.delete(library)
    await db.commit()
    return {'message': 'Data removed successfully'}
