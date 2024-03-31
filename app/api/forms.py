from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import FormSchemas
from app.models.form import Form
from app.schemas import FormCreate, FormUpdate

router_forms = APIRouter(prefix="/forms", tags=["forms"])


# CRUD operations for Form
@router_forms.get("/")
def get_forms(db: Session = Depends(get_db)) -> List[FormSchemas]:
    return db.query(Form).all()

@router_forms.post("/")
def create_form(form_data: FormCreate, db: Session = Depends(get_db)) -> FormSchemas:
    form = Form(**form_data.dict())
    db.add(form)
    db.commit()
    db.refresh(form)
    return form

@router_forms.get("/{form_id}")
def get_form(form_id: int, db: Session = Depends(get_db)) -> FormSchemas:
    form = db.query(Form).filter(Form.id == form_id).first()
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    return form

@router_forms.put("/{form_id}")
def update_form(form_id: int, form_data: FormUpdate, db: Session = Depends(get_db)) -> FormSchemas:
    form = db.query(Form).filter(Form.id == form_id).first()
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    for key, value in form_data.dict().items():
        setattr(form, key, value)
    db.commit()
    db.refresh(form)
    return form

@router_forms.delete("/{form_id}")
def delete_form(form_id: int, db: Session = Depends(get_db)):
    form = db.query(Form).filter(Form.id == form_id).first()
    if form is None:
        raise HTTPException(status_code=404, detail="Form not found")
    db.delete(form)
    db.commit()
    return {"detail": "Form deleted successfully"}
