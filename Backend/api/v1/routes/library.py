from fastapi import APIRouter
from fastapi.params import Depends
from Backend.app.api.v1.models import Library
from Backend.app.api.v1 import services

router = APIRouter(
    prefix='/library',
    tags=['library']
)


@router.get('/')
async def get_libraries(library: Library = Depends(services.search_all_libraries)):
    return library


@router.get('/search')
async def get_libraries_by_name_and_location(library: Library = Depends(services.search_library_by_name_and_location)):
    return library


@router.get('/id/{institution_id}')
async def get_institution_by_id(library: Library = Depends(services.search_library_by_id)):
    return library


@router.get('/name/{institution_name}')
async def get_institution_by_name(library: Library = Depends(services.search_library_by_name)):
    return library

@router.get('/location/{location}')
async def get_institution_by_location(library: Library = Depends(services.search_library_by_location)):
    return library