from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional, Annotated
from datetime import datetime
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]


class Question(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    question: str
    answer: str = None 
    created_at: datetime = None



class QuestionRequest(BaseModel):
    question: str
