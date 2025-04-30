from fastapi import APIRouter
from app.service.service import ask_question, get_all_questions, get_question_by_id
from app.models.questions import Question
from app.models.questions import QuestionRequest
router = APIRouter()

@router.post("/ask", tags=["questions"])
async def ask_agent(request: QuestionRequest):
    print("ask_agent")
    answer = await ask_question(request.question)
    return answer

@router.get("/questions", tags=["questions"])
async def list_questions():
    questions = await get_all_questions()
    return questions

@router.get("/questions/{id}", tags=["questions"])
async def get_question(id: str):
    question = await get_question_by_id(id)
    if question:
        return question
    else:
        return {"error": "Question not found"}