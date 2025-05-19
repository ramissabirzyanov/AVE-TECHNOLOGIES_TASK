from pydantic import BaseModel


class PhoneNumber(BaseModel):
    phone: int


class Data(PhoneNumber):
    address: str
