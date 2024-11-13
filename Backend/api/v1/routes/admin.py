from fastapi import APIRouter, Depends
from Backend.app.api.v1 import services, models

router = APIRouter(
    prefix='/admin'
)

# Library routes
@router.post('/library/create')
async def create_new_library(library: models.Library = Depends(services.add_library)):
    return library

@router.post('/library/bulk_create')
async def bulk_create_libraries(response: str = Depends(services.bulk_add_libraries)):
    return response




