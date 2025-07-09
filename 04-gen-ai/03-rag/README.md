# 🔍 03-rag: Retrieval-Augmented Generation (RAG)

This module covers everything you need to know about **Retrieval-Augmented Generation (RAG)** — a powerful technique to improve the factual accuracy of LLM outputs by injecting relevant context from external sources like documents or vector databases.

---

## 🧠 What is RAG?

> Retrieval-Augmented Generation (RAG) combines a **retriever** (to fetch relevant data) and a **generator** (to produce answers based on that data).

- It addresses the **hallucination problem** of LLMs by grounding responses in real-world documents.
- This is especially useful for domain-specific applications, long documents, and real-time information retrieval.

> 📖 *Learn more: [AWS — What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)*

---

## 📂 Folder Structure

```
03-rag/
├── assets/                        # Sample data, PDFs, or embedding outputs
├── langchain/                    # LangChain-based RAG examples
│   └── chatbot-retriever-memory.ipynb
├── 01-intro-to-rag.md            # Conceptual overview of RAG
├── 02-embeddings.ipynb           # Generate and explore text embeddings
├── 03-retrievers.ipynb           # Create retrievers with FAISS, Chroma, etc.
├── 04-vectorstores.ipynb         # Store and query embeddings from vector DBs
├── 05.1-rag-openai.ipynb         # Full RAG pipeline using OpenAI
├── 05.2-rag-ollama.py            # RAG pipeline using Ollama (local LLM)
└── README.md
└── requirements.txt
└── .env.example

```

---

## 📘 Notebooks Summary

| File | Description |
|------|-------------|
| `01-intro-to-rag.md` | High-level explanation of RAG architecture and use cases |
| `02-embeddings.ipynb` | Generate vector embeddings using Hugging Face or OpenAI |
| `03-retrievers.ipynb` | Retrieve relevant documents using similarity search |
| `04-vectorstores.ipynb` | Index, store, and query chunks using FAISS or Chroma |
| `05.1-rag-openai.ipynb` | End-to-end OpenAI-based RAG pipeline |
| `05.2-rag-ollama.py` | RAG using Ollama for local LLM inference |
| `langchain/chatbot-retriever-memory.ipynb` | Conversational RAG agent with memory using LangChain |

---

## 🛠️ Key Concepts Covered

- Tokenization and embedding generation
- Vector store construction (FAISS, Chroma)
- Prompt design for context injection
- Evaluation of retrieved vs. generated output
- Integration with LangChain and Ollama

---

## 🎯 Learning Goals

- Understand the anatomy of a RAG pipeline
- Implement chunking, embedding, retrieval, and generation
- Explore both OpenAI-hosted and local LLM options (Ollama)
- Build RAG-based chat systems with memory (LangChain)

---

## 📚 References

- AWS Docs: [What is RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- Udemy Course: [Agentic AI Bootcamp (LangGraph + LangChain)](https://www.udemy.com/course/complete-agentic-ai-bootcamp-with-langgraph-and-langchain)

---