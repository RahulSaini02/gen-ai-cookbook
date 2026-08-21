# RAG Projects

Applied, curriculum-driven RAG builds, migrated in from the standalone
`forward-deployed-ai-engineer` repo. See
[`agentic-ai-mastery-notebook.md`](agentic-ai-mastery-notebook.md) for the
module-by-module curriculum these projects work through.

## Projects

| Project | Description |
|---------|-------------|
| [`customer-support-agent/`](customer-support-agent/) | Week 4: Naive RAG system for e-commerce customer support — retrieves customer/order data and policy docs to answer support queries. |
| [`hybrid-retrieval/`](hybrid-retrieval/) | Scaffold for a hybrid (sparse + dense) retrieval project — not yet implemented. |

## Setup

1. Install shared dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure Ollama is running (for local embeddings/LLM):
```bash
ollama serve
```

3. See [`customer-support-agent/README.md`](customer-support-agent/README.md) for
   that project's dataset, setup, and usage details.
