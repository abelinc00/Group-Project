from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import feedback as controller
from ..schemas import feedback as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Feedback'],
    prefix="/feedback"
)


@router.post("/", response_model=schema.Feedback, status_code=status.HTTP_201_CREATED)
def create(request: schema.FeedbackCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Feedback])
def read_all(db: Session = Depends(get_db)):
    """Get all feedback entries"""
    return controller.read_all(db)


@router.get("/{feedback_id}", response_model=schema.Feedback)
def read_one(feedback_id: int, db: Session = Depends(get_db)):
    feedback = controller.read_one(db=db, feedback_id=feedback_id)
    return feedback


@router.put("/{feedback_id}", response_model=schema.Feedback)
def update(feedback_id: int, request: schema.FeedbackCreate, db: Session = Depends(get_db)):
    updated_feedback = controller.update(db=db, feedback_id=feedback_id, request=request)
    return updated_feedback


@router.delete("/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(feedback_id: int, db: Session = Depends(get_db)):
    result = controller.delete(db=db, feedback_id=feedback_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
