from pydantic import BaseModel

class OrderManagementCreate(BaseModel):
    order_id: int
    customer_name: str
    order_status: str


class OrderManagementRead(OrderManagementCreate):
    id: int

    class Config:
        orm_mode = True
