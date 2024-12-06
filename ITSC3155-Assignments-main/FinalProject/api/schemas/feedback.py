from pydantic import BaseModel

class FeedbackBase(BaseModel):
    order_id: int
    feedback_text: str
    rating: int

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int

    class ConfigDict:
        from_attributes = True

