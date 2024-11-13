from fastapi import APIRouter
from app.api.v1.db import DB_Session
from app.api.v1.schemas import LibraryCreate
from app.api.v1.services import create_library

router = APIRouter(
    prefix='/library',
    tags=['library']
)

@router.post('/')
async def create_new_library(library: LibraryCreate, db:DB_Session):
    return await create_library(db, library)