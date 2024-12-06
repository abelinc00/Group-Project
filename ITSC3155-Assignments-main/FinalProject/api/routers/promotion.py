from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotion as controller
from ..schemas import promotion as schema
from ..dependencies.database import get_db
router = APIRouter(
    tags=['Promotion'],
    prefix="/promotion"
)
@router.post("/", response_model=schema.Promotion, status_code=status.HTTP_201_CREATED)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create_promotion(db=db, request=request)
@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    """Get all promotions"""
    return controller.get_promotion(db)
@router.get("/{promotion_id}", response_model=schema.Promotion)
def read_one(promotion_id: int, db: Session = Depends(get_db)):
    promotion = controller.get_promotion(db=db, promotion_id=promotion_id)
    return promotion
@router.put("/{promotion_id}", response_model=schema.Promotion)
def update(promotion_id: int, request: schema.PromotionCreate, db: Session = Depends(get_db)):
    updated_feedback = controller.update_promotion(db=db, promotion_id=promotion_id, request=request)
    return updated_feedback
@router.delete("/{promotion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(promotion_id: int, db: Session = Depends(get_db)):
    result = controller.delete_promotion(db=db, promotion_id=promotion_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)