from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(String(255))
    category = Column(String(50))
