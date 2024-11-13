from fastapi import APIRouter, Depends
from Backend.api.v1 import services, models
from typing import List, Union, Dict
router = APIRouter(
    prefix='/v1/admin'
)

# Library routes
@router.post('/library/create')
async def create_new_library(library: models.Library = Depends(services.add_library)):
    return library

@router.post('/library/bulk_create')
async def bulk_create_libraries(response: Dict[str, Union[str, List]] = Depends(services.bulk_add_libraries)):
    return response

@router.delete('/library/')
async def bulk_create_libraries(response: Dict[str, str] = Depends(services.remove_library)):
    return response




