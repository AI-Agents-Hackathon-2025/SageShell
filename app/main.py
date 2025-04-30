from fastapi import FastAPI
from app.controllers.controller import router as question_router

app = FastAPI(
    title="SageShell",
    description=(
        "SageShell is a smart terminal-based assistant that uses real-time DuckDuckGo search combined with "
        "Hugging Face's NLP model (DistilBERT) to provide accurate, contextual answers to user questions. "
        "Runs entirely locally, with no need for cloud services."
    ),
    version="1.0.0"
)

app.include_router(question_router)
