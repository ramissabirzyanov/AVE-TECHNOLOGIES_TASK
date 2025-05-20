from pydantic import BaseModel


class DataSchema(BaseModel):
    phone: int
    address: str


class DataResponseSchema(BaseModel):
    address: str
