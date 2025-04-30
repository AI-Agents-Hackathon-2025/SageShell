# 🧠 SageShell – A Smart Terminal-Based AI Assistant

**Theme**: A local command-line assistant that combines real-time web search with intelligent, contextual answers using NLP. Powered by DuckDuckGo Search and Hugging Face Transformers.

---

## 📌 Description

**SageShell** is a lightweight, terminal-based AI agent developed by **Rafael**, **Daniel**, and **Mateus** on **04/11/2025**.  
It allows users to ask natural language questions and get contextual, AI-generated answers using real-time search results from **DuckDuckGo**.

Using the **DistilBERT (SQuAD)** model from Hugging Face, SageShell extracts relevant answers from search data and presents concise, accurate responses — all running locally, without cloud dependency.

---

## 🚀 Features

- 🔍 Real-time search via DuckDuckGo  
- 🧠 AI-powered question answering with `distilbert-base-uncased-distilled-squad`  
- 💬 Fully interactive in the terminal  
- 🔒 Runs locally without storing or transmitting user data  
- 🧩 Modular design: easy to extend or customize  
- 🗃️ API endpoints to interact with stored questions and answers

---

## 📦 Technologies Used

- **Python 3.10+**
- [`duckduckgo-search`](https://pypi.org/project/duckduckgo-search/)
- [`transformers`](https://huggingface.co/transformers/)
- [`torch`](https://pytorch.org/)
- Model: `distilbert-base-uncased-distilled-squad` (from Hugging Face)
- **FastAPI** for building the API
- **MongoDB** for storing questions and answers

---


## 🛠️ API Routes

### 1. POST /ask

This endpoint allows you to ask a question to the AI agent.

Request:
```bash
{
  "question": "What is the theory of relativity?"
}
```
Response:

```bash
{
  "answer": "The theory of relativity, developed by Albert Einstein, describes the laws of physics in relation to objects moving at high speeds and the nature of gravity. It consists of two parts: special relativity and general relativity."
}
```
### 2. GET /questions

This endpoint allows you to retrieve all stored questions.

Response:
```bash
[
  {
    "question": "What is the theory of relativity?",
    "answer": "The theory of relativity, developed by Albert Einstein, describes the laws of physics in relation to objects moving at high speeds and the nature of gravity."
  },
  ...
]
```

### 3. GET /questions/{id}

This endpoint allows you to retrieve a specific question by its id.

Response:

```bash
{
  "question": "What is the theory of relativity?",
  "answer": "The theory of relativity, developed by Albert Einstein, describes the laws of physics in relation to objects moving at high speeds and the nature of gravity."
}
```

## 👥 Authors

- [Rafael Loureiro](https://github.com/rafaelloureiroc)   
- [Daniel Ugulino](https://github.com/Daniel-Ugulino)  
- [Mateus Oliveira](https://github.com/Mateusol22  )   
