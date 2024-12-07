from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.order_management import OrderManagement
from ..schemas.order_management import OrderManagementCreate, OrderManagementRead

router = APIRouter(
    prefix="/order_management",
    tags=["Order Management"],
)

@router.get("/", response_model=list[OrderManagementRead])
def get_all_orders(db: Session = Depends(get_db)):
    return db.query(OrderManagement).all()


@router.get("/{order_id}", response_model=OrderManagementRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderManagement).filter(OrderManagement.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/", response_model=OrderManagementRead)
def create_order(order: OrderManagementCreate, db: Session = Depends(get_db)):
    new_order = OrderManagement(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order



@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderManagement).filter(OrderManagement.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": f"Order with ID {order_id} deleted successfully"}
