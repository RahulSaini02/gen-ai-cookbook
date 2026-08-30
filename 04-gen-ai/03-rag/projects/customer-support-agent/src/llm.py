"""LLM abstraction with local/cloud fallback."""

import requests
from config import DEFAULT_LLM_MODEL, DEFAULT_LLM_TIER, OLLAMA_TIMEOUT, OLLAMA_URL
from ollama import ResponseError, chat


def is_ollama_active() -> bool:
    """Check whether Ollama is running locally."""
    try:
        response = requests.get(f"{OLLAMA_URL}/", timeout=OLLAMA_TIMEOUT)
        return response.status_code == 200
    except requests.RequestException:
        return False


def generate(
    message: str,
    messages: list,
    model: str = DEFAULT_LLM_MODEL,
    tier: str = DEFAULT_LLM_TIER,
    think: str | None = None,
) -> str | None:
    """Generate a response using either local or cloud Ollama."""

    messages.append({"role": "user", "content": message})

    try:
        if tier == "cloud":
            response = chat(
                model=model,
                messages=messages,
                think=think,
            )

        elif tier == "local":
            if not is_ollama_active():
                print("Ollama is not running.")
                return None

            response = chat(
                model=model,
                messages=messages,
                think=think,
            )

        else:
            raise ValueError(f"Invalid tier: {tier}")

        if response.message.content:
            messages.append(
                {
                    "role": "assistant",
                    "content": response.message.content,
                }
            )

        return response.message.content

    except ResponseError as e:
        print(f"Ollama error: {e}")
        return None