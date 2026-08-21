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
    """Generate response from LLM with local/cloud fallback."""
    messages.append({"role": "user", "content": message})

    try:
        if tier == "local":
            if is_ollama_active():
                try:
                    response = chat(model=model, messages=messages, think=think)
                except ResponseError:
                    print(f"Local model '{model}' not available.")
                    print("Falling back to Ollama Cloud...")
                    response = chat(
                        model=f"{model}:cloud", messages=messages, think=think
                    )
            else:
                print("Ollama is not running.")
                print("Falling back to Ollama Cloud...")
                response = chat(model=f"{model}:cloud", messages=messages, think=think)
        else:
            response = chat(model=f"{model}:cloud", messages=messages, think=think)

        if response.message.content:
            messages.append({"role": "assistant", "content": response.message.content})

        return response.message.content

    except ResponseError as e:
        print(f"Ollama error: {e}")
        return None
