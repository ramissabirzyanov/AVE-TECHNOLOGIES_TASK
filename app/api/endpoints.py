from fastapi import APIRouter, Depends, HTTPException, status, responses, Query

from app.api.schemas import DataSchema, AddressSchema
from app.services.app_service import AppService
from app.api.dependencies import get_service
from app.core.logger import logger


router = APIRouter()


# @router.get('/data/{phone}', response_model=AddressSchema)
# async def chech_data(phone: str, service: AppService = Depends(get_service)):
#     address = await service.check_data_by_phone(phone)
#     logger.debug(f"data for {phone}: {address}")
#     if not address:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No data for {phone}"
#         )
#     return AddressSchema(address=address)


@router.get('/data', response_model=AddressSchema)
async def check_data(
    phone: str = Query(..., description="Phone number to find data"),  # Обязательный параметр
    service: AppService = Depends(get_service)
):
    address = await service.check_data_by_phone(phone)
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data for {phone}"
        )
    return AddressSchema(address=address)


@router.post('/data')
async def write_data(data: DataSchema, service: AppService = Depends(get_service)):
    logger.debug(f"data in request {data.phone}: {data.address}")
    await service.write_data(data)
    return responses.JSONResponse(status_code=201, content={"message": "Data was written."})


@router.put('/data/{phone}')
async def update_data(phone: str, data: AddressSchema, service: AppService = Depends(get_service)):
    try:
        await service.update_data_by_phone(phone, data)
        return responses.JSONResponse(status_code=200, content={"message": "Data was rewritten."})
    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e
        )
