# 🧠 LangChain

This repository documents a structured and hands-on learning path through the **LangChain framework**, focusing on how to build LLM-powered applications using tools like Groq, OpenAI, Ollama, vector databases, and FastAPI.

---

## 📚 Structure & Topics

The content is divided into topic-based folders following a chronological learning flow:

### 01. 🧩 Intro to Pydantic
- Basics of Pydantic — crucial for FastAPI, LangServe, and LangChain schemas.
- 📘 `intro-to-pydantic.ipynb`

---

### 02. ⚙️ LangChain Fundamentals
- Overview of key LangChain components (prompts, chains, memory, models).
- Building a basic chatbot with message history.
- 📘 `langchain-components-overview.md`
- 📘 `chatbot-message-history.ipynb`

---

### 03. 📥 Data Ingestion
- Using document loaders (PDFs, HTML, APIs, etc.)
- Splitting text into manageable chunks.
- 📘 `document-loaders.ipynb`
- 📘 `text-splitters.ipynb`
- 📁 `data/` — Raw sample PDFs, articles, etc.

---

### 04. 🧠 Embeddings & VectorStores
- Creating text embeddings.
- Working with vector databases (FAISS, Chroma).
- Implementing retrievers.
- 📘 `embeddings.ipynb`
- 📘 `vectorstores.ipynb`
- 📘 `retrievers.ipynb`

---

### 05. 🔁 Retrieval Augmented Generation (RAG)
- Building RAG pipelines using:
  - OpenAI (`rag-openai.ipynb`)
  - Ollama (`rag-ollama.py`)

---

### 06. 🕹️ Agents & Agentic Workflows
- Difference between agents and traditional chains.
- Intro to ReAct, Tool use, and decision-making with LLMs.
- 📘 `agents-vs-agentic-ai.md`

---

## 🚀 FastAPI + LangServe App

The `app/` folder contains the LangServe server code exposing LangChain chains via API:
- `/chain` endpoint using Groq's LLMs
- Built using `FastAPI`, `LangServe`, and `ChatGroq`
- 📁 `app/serve.py`

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/RahulSaini02/gen-ai-cookbook.git
   cd 04-gen-ai/langchain
   ```

2. Set up the virtual environment
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

3. Add your .env

  ```bash
  cp .env.example .env
  ```

## 🛠 Tech Stack
🧠 LangChain (chains, retrievers, memory)

🌐 FastAPI + LangServe

🔗 Groq LLMs, OpenAI API, Ollama LLMS

📄 Document Loaders (PDF, web)

🧾 Vector DBs: FAISS, Chroma

🧪 Jupyter Notebooks