from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotion"

    promotion_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    promotion_code = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    discount_percentage = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    expiration_data = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

