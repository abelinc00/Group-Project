from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promotion as model
from sqlalchemy.exc import SQLAlchemyError
from ..dependencies.database import get_db


def create_promotion(db: Session, request):
    new_promotion = model.Promotion(
        promotion_id=request.promotion_id,
        customer_name=request.customer_name,
        promotion_code=request.promotion_code,
        discount_percentage=request.discount_percentage,
        expiration_data=request.expiration_data
    )

    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_promotion


# Get promotions
def get_promotion(db: Session = Depends(get_db)):
    promotion = db.query(model.Promotion).filter(model.Promotion.id == id).first()
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found",
        )
    return promotion


def update_promotion(request: model.Promotion, db: Session = Depends(get_db)):
    try:
        promotion = db.query(model.Promotion).filter(model.Promotion.id == id)
        if not promotion.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        update_data = request.dict(exclude_unset=True)
        promotion.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promotion.first()


def delete_promotion(db: Session, promotion_id):
    try:
        promotion = db.query(model.Promotion).filter(model.Promotion.id == id)
        if not promotion.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        promotion.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
