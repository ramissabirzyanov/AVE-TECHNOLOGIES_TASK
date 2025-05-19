from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas import Data


router = APIRouter()


@router.get('/check_data')
async def chech_data():
    pass



@router.post('/write_data', response_model=Data)
async def write_data():
    pass
