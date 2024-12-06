from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..models import feedback as model
from ..dependencies.database import get_db
from sqlalchemy.exc import SQLAlchemyError



# Create Feedback
def create_feedback(request: model.Feedback, db: Session = Depends(get_db)):
    new_feedback = model.Feedback(
        order_id=request.order_id,
        feedback_text=request.feedback_text,
        rating=request.rating
    )
    try:
        db.add(new_feedback)
        db.commit()
        db.refresh(new_feedback)
        return new_feedback
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)


# Get Feedback
def get_feedback(db: Session = Depends(get_db)):
    feedback = db.query(model.Feedback).filter(model.Feedback.id == id).first()
    if not feedback:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found",
        )
    return feedback


# Update Feedback
def update_feedback(request: model.Feedback, db: Session = Depends(get_db)):
    feedback = db.query(model.Feedback).filter(model.Feedback.id == id).first()
    if not feedback:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found",
        )
    try:
        feedback.feedback_text = request.feedback_text
        feedback.rating = request.rating
        db.commit()
        db.refresh(feedback)
        return feedback
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)


# Delete Feedback
def delete_feedback(db: Session = Depends(get_db)):
    feedback = db.query(model.Feedback).filter(model.Feedback.id == id).first()
    if not feedback:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found",
        )
    try:
        db.delete(feedback)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)
