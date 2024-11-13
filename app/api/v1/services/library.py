from sqlalchemy import select
from app.api.v1.models import Library
from app.api.v1.schemas import LibraryCreate
from app.api.v1.db import DB_Session


async def create_library(db: DB_Session, library: LibraryCreate):
    try:
        exists = await db.scalars(select(Library).where(Library.institution_name == library.institution_name))
        if exists.all():
            return {'error': 'Library already exists.'}
        new_library = Library(**library.model_dump())
        db.add(new_library)
        await db.commit()
        return library
    except Exception as e:
        print(e)

