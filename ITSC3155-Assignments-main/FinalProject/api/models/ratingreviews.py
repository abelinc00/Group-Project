from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class RatingReview(Base):
    __tablename__ = "ratings_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    review_text = Column(String(500), nullable=True)  # Optional, max 500 characters
    score = Column(Integer, nullable=False)  # Assuming a 1-5 rating scale

    customer = relationship("Customer", back_populates="ratings_reviews")
    menu_item = relationship("MenuItem", back_populates="ratings_reviews")
