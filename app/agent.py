from duckduckgo_search import DDGS
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Função para buscar no DuckDuckGo
async def search_duckduckgo(question: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(question, max_results=3)
        answers = [r["body"] for r in results]
        return "\n".join(answers[:2]) if answers else ""

# Função para gerar a resposta com o modelo de QA
async def generate_answer(question: str, context: str) -> str:
    if not context.strip():
        return "I couldn't find enough information to answer that."
    result = qa_pipeline(question=question, context=context)
    return result["answer"]