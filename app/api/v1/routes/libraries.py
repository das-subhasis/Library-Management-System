from fastapi import APIRouter
from database.database import DBSession
from sqlalchemy import select
from models.library import Library

router = APIRouter(
    prefix='/library',
    tags=['library']
)

@router.get('/')
async def get_all_libraries(db:DBSession):
    res = await db.scalars(select(Library)).all()
    return