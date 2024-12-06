from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    feedback_text = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)
