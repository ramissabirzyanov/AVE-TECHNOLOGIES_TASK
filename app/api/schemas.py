from pydantic import BaseModel


class AddressSchema(BaseModel):
    address: str


class DataSchema(AddressSchema):
    phone: int
