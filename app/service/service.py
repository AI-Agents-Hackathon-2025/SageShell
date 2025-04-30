from app.database import questions_collection
from app.models.questions import Question
from app.agent import search_duckduckgo, generate_answer
from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException

async def ask_question(question: str) -> dict:
    if not question.strip():
        raise ValueError("A pergunta não pode estar vazia.")

    context = await search_duckduckgo(question)
    answer = await generate_answer(question, context)

    question_data = {
        "question": question,
        "answer": answer,
        "created_at": datetime.utcnow()
    }

    result = await questions_collection.insert_one(question_data)
    
    question_data["id"] = str(result.inserted_id)

    return {
        "id": question_data["id"],
        "question": question,
        "answer": answer,
        "created_at": question_data["created_at"]
    }


async def get_all_questions():
    questions_cursor = await questions_collection.find().to_list()
    return [Question(**question) for question in questions_cursor]

async def get_question_by_id(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    question_data = await questions_collection.find_one({'_id': object_id})
    
    if question_data is None:
        raise HTTPException(status_code=404, detail='Question not found.')
    
    return Question(**question_data)