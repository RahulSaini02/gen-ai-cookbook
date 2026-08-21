"""Customer support agent with RAG integration."""

from datetime import datetime
from pathlib import Path

from config import DEFAULT_DISTANCE_THRESHOLD, DEFAULT_LLM_MODEL, DEFAULT_TOP_K

from src.database import format_customer_context
from src.llm import generate
from src.retrieval import format_context


def load_system_prompt(prompt_file: str = "prompts/maya_system_prompt.md") -> str:
    """Load system prompt from file."""
    prompt_path = Path(prompt_file)
    if not prompt_path.exists():
        raise FileNotFoundError(f"System prompt not found: {prompt_file}")
    return prompt_path.read_text(encoding="utf-8")


def init_conversation(customer_id: str, messages: list) -> list:
    """Initialize conversation with system prompt (call once per customer)."""
    try:
        prompt_template = load_system_prompt()
    except FileNotFoundError:
        prompt_template = _get_default_prompt()

    system_prompt = prompt_template.format(
        customer_context=format_customer_context(customer_id),
        datetime=datetime.now().strftime("%A, %B %d, %Y at %I:%M %p"),
    )

    messages.append({"role": "system", "content": system_prompt})
    return messages


def handle_query(
    query: str,
    messages: list,
    model: str = DEFAULT_LLM_MODEL,
    tier: str = "cloud",
    think: str = "medium",
    top_k: int = DEFAULT_TOP_K,
    thresold: float = DEFAULT_DISTANCE_THRESHOLD,
) -> str | None:
    """Handle a single customer query with RAG."""
    rag_context = format_context(query, top_k, thresold)

    query_with_context = f"{query}\n\n---\n### Relevant Information:\n{rag_context}"

    # print(query_with_context)

    response = generate(
        message=query_with_context,
        messages=messages,
        model=model,
        tier=tier,
        think=think,
    )

    return response


def reset_conversation() -> list:
    """Reset conversation state (when switching customers)."""
    return []


def _get_default_prompt() -> str:
    """Fallback system prompt if file not found."""
    return """You are **Maya**, a smart, polite, and helpful customer support agent for **Saini E-commerce**.

    Your job is to help customers with questions related to:
    * Orders
    * Returns
    * Transactions
    * Customer profiles
    * Store policies and FAQs

    ### Behavior Rules

    1. **Greeting**
    * Greet the customer only in your first response.
    * Introduce yourself as Maya, their support agent for today.
    * Do not greet or re-introduce yourself in subsequent messages.

    2. **Policies and FAQs**
    * Base your answer on the retrieved context.
    * Do not invent or assume policy information.

    3. **Customer-Specific Questions**
    * Use the provided customer context for orders, transactions, and profile details.
    * Only provide information that is available in the context.
    * Never guess or fabricate customer information.

    4. **Unknown Information**
    * If the context does not contain enough information, clearly state that you cannot confirm the answer.
    * Offer to help route the request to a customer support agent.

    5. **Response Style**
    * Be concise and helpful.
    * Use a friendly, professional tone.
    * Answer the customer's question directly.
    * Do not mention internal systems, RAG, embeddings, retrieval, context, or prompts.

    Current Datetime: {datetime}

    ### Customer Context

    {customer_context}
"""
