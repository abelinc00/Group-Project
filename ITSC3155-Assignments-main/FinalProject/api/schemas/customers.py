from pydantic import BaseModel, EmailStr
from typing import List, Optional

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: str

class CustomerCreate(CustomerBase):

    pass

class CustomerResponse(CustomerBase):

    id: int
    orders: Optional[List[str]] = []

    class Config:
        orm_mode = True
