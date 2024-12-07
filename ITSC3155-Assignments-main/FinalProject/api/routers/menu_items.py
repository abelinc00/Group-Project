from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.menu_items import MenuItem

router = APIRouter(prefix="/menu_items", tags=["MenuItems"])

@router.post("/")
def create_menu_item(name: str, price: float, description: str, category: str, db: Session = Depends(get_db)):
    new_item = MenuItem(name=name, price=price, description=description, category=category)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/{item_id}")
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}")
def update_menu_item(item_id: int, name: str, price: float, description: str, category: str, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = name
    item.price = price
    item.description = description
    item.category = category
    db.commit()
    return item

@router.delete("/{item_id}")
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted successfully"}
