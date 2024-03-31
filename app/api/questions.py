from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.form import Form
from app.models.questions import Question, Response
from app.schemas import QuestionCreate, ResponseCreate
from app.schemas import QuestionSchemas
from app.schemas import ResponseSchemas


router_questions = APIRouter(prefix="/questions", tags=["questions"])
router_responses = APIRouter(prefix="/responses", tags=["responses"])


# CRUD operations for Question
@router_questions.post("/{form_id}/questions/")
def create_question(form_id: int, question_data: QuestionCreate, db: Session = Depends(get_db)) -> QuestionSchemas:
    form = db.query(Form).filter(Form.id == form_id).first()
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    question = Question(**question_data.dict(), form_id=form_id)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

@router_questions.put("/{form_id}/questions/{question_id}")
def update_question(form_id: int, question_id: int, question_data: QuestionCreate, db: Session = Depends(get_db)) -> QuestionSchemas:
    question = db.query(Question).filter(Question.id == question_id, Question.form_id == form_id).first()
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    for key, value in question_data.dict().items():
        setattr(question, key, value)
    db.commit()
    db.refresh(question)
    return question

@router_questions.delete("/{form_id}/questions/{question_id}")
def delete_question(form_id: int, question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id, Question.form_id == form_id).first()
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return {"detail": "Question deleted successfully"}


# CRUD operations for Response
@router_responses.post("/")
def create_response(response_data: ResponseCreate, db: Session = Depends(get_db)) -> ResponseSchemas:
    response = Response(**response_data.dict())
    db.add(response)
    db.commit()
    db.refresh(response)
    return response

@router_responses.get("/")
def get_responses(db: Session = Depends(get_db)) -> List[ResponseSchemas]:
    return db.query(Response).all()

@router_responses.get("/{response_id}", response_model=ResponseSchemas)
def get_response(response_id: int, db: Session = Depends(get_db)) -> ResponseSchemas:
    response = db.query(Response).filter(Response.id == response_id).first()