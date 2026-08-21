# Customer Support Agent - Module Structure

Production-quality code organization for Week 4 Naive RAG.

## Module Breakdown

### `database.py` - SQLite Operations
**Purpose:** Structured queries for customer and order data  
**Key Functions:**
- `get_customer(customer_id)` - Customer lookup
- `get_order(order_id)` - Order lookup with items
- `get_customer_orders(customer_id)` - All orders for customer
- `format_customer_context(customer_id)` - Format for LLM
- `format_order_context(order_id)` - Format for LLM

**When to use:** For exact, deterministic queries (customer tiers, order status)

---

### `embeddings.py` - Document Processing
**Purpose:** Load and embed documents (PDF, Markdown, Text)  
**Key Functions:**
- `load_document(file_path)` - Smart loader (detects PDF vs text)
- `load_pdf(file_path)` - PDF-specific loading
- `load_text_file(file_path)` - Markdown/text loading
- `chunk_text(text, chunk_size, overlap)` - Split into overlapping chunks
- `embed(text, model)` - Generate embeddings via Ollama
- `generate_embeddings(library)` - Batch embed all docs in directory

**When to use:** Setting up RAG pipeline with policies, FAQs, documentation

---

### `retrieval.py` - Vector Database
**Purpose:** ChromaDB queries and context formatting  
**Key Functions:**
- `get_collection()` - Connect to ChromaDB
- `query_research(query, top_k, threshold)` - Semantic search
- `format_context(query, top_k, threshold)` - Format results for LLM

**When to use:** Retrieving relevant policies, FAQs, documentation

---

### `llm.py` - Language Model Abstraction
**Purpose:** Unified LLM interface with local/cloud fallback  
**Key Functions:**
- `is_ollama_active()` - Check if Ollama running locally
- `generate(message, messages, model, tier)` - Generate response
  - Tries local Ollama first
  - Falls back to Ollama Cloud if local fails
  - Maintains message history

**When to use:** Generating responses with context

---

### `agent.py` - Conversation Management
**Purpose:** High-level agent loop combining all modules  
**Key Functions:**
- `init_conversation(customer_id, messages)` - Initialize with system prompt
  - Loads prompt template from file
  - Injects customer context
  - Sets up message history
- `handle_query(query, messages)` - Process single customer query
  - Retrieves RAG context
  - Calls LLM with combined context
  - Returns response
- `reset_conversation()` - Clear messages (switch customers)

**When to use:** Main entry point for customer interactions

---

### `evals.py` - Evaluation & Testing
**Purpose:** Measure agent quality (correctness, safety, tone)  
**Key Classes:**
- `EvalCase` - A single test case (query, expected keywords, forbidden keywords)
- `EvalResult` - Results from running one eval case

**Key Functions:**
- `run_eval_suite(cases)` - Run all tests, print results
- `save_eval_results(results, prompt_version)` - Save to JSON with timestamp

**When to use:** Validating agent behavior before deployment

---

## Quick Usage

### Basic Query
```python
from src.agent import init_conversation, handle_query

messages = []
init_conversation("CUST001", messages)
response = handle_query("What's your return policy?", messages)
print(response)
```

### Evaluation
```python
from src.evals import EvalCase, run_eval_suite, save_eval_results

eval_cases = [
    EvalCase(
        customer_id="CUST001",
        query="What's your return policy?",
        expected_keywords=["30 days", "return"],
        forbidden_keywords=["unsure"],
        description="Return policy question"
    ),
]

results = run_eval_suite(eval_cases)
save_eval_results(results, prompt_version="v1")
```

### Generate Embeddings
```python
from src.embeddings import generate_embeddings
from pathlib import Path

embeddings = generate_embeddings(Path("./data/docs"))
print(f"Generated {len(embeddings)} chunks")
```

---

## Data Flow

```
Customer Query
    ↓
[agent.py] init_conversation()
    ↓ (loads system prompt)
[database.py] format_customer_context()
    ↓ (retrieves customer info)
[agent.py] handle_query()
    ├→ [retrieval.py] format_context()
    │   └→ [retrieval.py] query_research()
    │       └→ ChromaDB semantic search
    │
    └→ [llm.py] generate()
        └→ Ollama (local or cloud)
    
    ↓
LLM Response
    ↓
[evals.py] (optional) evaluate response quality
```

---

## Production Checklist

- [x] Smart document loading (PDF, MD, TXT)
- [x] Modular architecture (separations of concerns)
- [x] Configuration management (config.py)
- [x] System prompt versioning (prompts/ directory)
- [x] Evaluation framework (src/evals.py)
- [x] LLM fallback strategy (local → cloud)
- [x] Message history tracking (multi-turn)
- [ ] Logging (add logging module)
- [ ] Rate limiting
- [ ] Error handling (add try/except in critical paths)
- [ ] Performance monitoring

---

## Next Steps for Production

1. **Add logging** - Track agent decisions and LLM calls
2. **Add error handling** - Graceful degradation on failures
3. **Add rate limiting** - Prevent abuse
4. **Expand evaluations** - More test cases, LLM-based grading
5. **Monitor performance** - Track latency, token usage, costs
6. **A/B test prompts** - Compare versions with evals
7. **Add security** - Rate limits, input validation, secrets management
