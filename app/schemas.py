from pydantic import BaseModel
from typing import Optional
from enum import Enum

class FormCreate(BaseModel):
    title: str
    description: Optional[str] = None


class FormUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class FormSchemas(BaseModel):
    id: int
    title: str
    description: Optional[str] = None


class QuestionCreate(BaseModel):
    text: str
    type: str


class QuestionUpdate(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None


class QuestionSchemas(BaseModel):
    id: int
    text: str
    type: str
    form_id: int


class ResponseCreate(BaseModel):
    question_id: int
    answer: str


class ResponseUpdate(BaseModel):
    question_id: Optional[int] = None
    answer: Optional[str] = None


class ResponseSchemas(BaseModel):
    id: int
    question_id: int
    answer: str

class QuestionType(str, Enum):
    single = "single"
    multiple = "multiple"
    text = "text"