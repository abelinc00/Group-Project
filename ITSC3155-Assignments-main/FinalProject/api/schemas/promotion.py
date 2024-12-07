from pydantic import BaseModel
class PromotionBase(BaseModel):
    promotion_id: int
    customer_name: str
    promotion_code: int
    discount_percentage: int
    expiration_data: int
class PromotionCreate(PromotionBase):
    pass
class Promotion(PromotionBase):
    id: int
    class ConfigDict:
        from_attributes = True