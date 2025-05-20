from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas import DataSchema, DataResponseSchema
from app.services.app_service import AppService
from app.api.dependencies import get_service
from app.core.logger import logger


router = APIRouter()


@router.get('/check_data', response_model=DataResponseSchema)
async def chech_data(phone: str, service: AppService = Depends(get_service)):
    address = await service.check_data_by_phone(phone)
    logger.debug(f"data for {phone}: {address}")
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data for {phone}"
        )
    return DataResponseSchema(address=address)


@router.post('/write_data')
async def write_data(data: DataSchema, service: AppService = Depends(get_service)):
    logger.debug(f"data in request {data.phone}: {data.address}")
    if await service.is_phone_exist(data.phone):
        await service.write_data(data)
        return {"detail": "Data was rewritten."}
    await service.write_data(data)
    return {"detail": "Data was written."}
