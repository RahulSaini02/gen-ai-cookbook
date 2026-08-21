"""Customer support agent source code."""

from src.agent import handle_query, init_conversation, reset_conversation
from src.database import (
    format_customer_context,
    format_order_context,
    get_customer,
    get_customer_orders,
    get_order,
)
from src.embeddings import (
    chunk_text,
    embed,
    generate_embeddings,
    load_document,
    load_pdf,
)
from src.evals import EvalCase, EvalResult, run_eval_suite, save_eval_results
from src.llm import generate, is_ollama_active
from src.retrieval import format_context, query_research

__all__ = [
    "EvalCase",
    "EvalResult",
    "chunk_text",
    "embed",
    "format_context",
    "format_customer_context",
    "format_order_context",
    "generate",
    "generate_embeddings",
    "get_customer",
    "get_customer_orders",
    "get_order",
    "handle_query",
    "init_conversation",
    "is_ollama_active",
    "load_document",
    "load_pdf",
    "query_research",
    "reset_conversation",
    "run_eval_suite",
    "save_eval_results",
]
