from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas import DataSchema, DataResponseSchema
from app.services.app_service import AppService
from app.api.dependencies import get_service
from app.core.logger import logger


router = APIRouter()


@router.get('/check_data', response_model=DataResponseSchema)
async def chech_data(phone: str, service: AppService = Depends(get_service)):
    data = await service.check_data_by_phone(phone)
    logger.debug(f"data for {phone}: {data}")
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No data for {phone}"
        )
    return DataResponseSchema(address=data)


@router.post('/write_data')
async def write_data(data: DataSchema, service: AppService = Depends(get_service)):
    logger.debug(f"data in request {data.phone}: {data.address}")
    await service.write_data(data)
    return {"detail": "Data was written."}
