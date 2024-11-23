from pydantic import BaseModel, Field, conint
from typing import Optional


class RatingReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    review_text: Optional[str] = Field(None, max_length=500)
    score: conint(ge=1, le=5)  # Rating must be between 1 and 5


class RatingReviewCreate(RatingReviewBase):
    """Schema for creating a new Rating & Review."""
    pass


class RatingReviewResponse(RatingReviewBase):
    """Schema for returning Rating & Review details."""
    id: int

    class Config:
        orm_mode = True
