from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(15), nullable=False)
    address = Column(String(300), nullable=False)

    # Relationship to other tables, if any
    orders = relationship("Order", back_populates="customer")  # Example: customer can have multiple orders
