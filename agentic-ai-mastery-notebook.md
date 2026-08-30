# Agentic AI Mastery Notebook
### Aug 2026 → Dec 2026 · Fundamentals to forward-deployed-ready

Built around your Wed (theory) / Fri (applied) / Sat (project) AI blocks — roughly 4 hrs/week, 22 weeks, Aug 3–Dec 31. Check items off as you go. This is meant to be revisited, not read once.

**Legend:** items marked **(review)** are things you already touch at work — revisit for depth, not first exposure. Everything else is new ground.

---

## The Project: Scout

A local-first agent that tracks what's actually new in agentic AI — arXiv papers, company engineering blogs, framework releases — and turns it into a running digest. Keeping this notebook itself current becomes part of what you're building.

**Why this project:** it gives the local/cloud split a real reason to exist instead of an arbitrary one. High-volume, low-stakes work — is this new, is it relevant — runs on a local model constantly and free. Low-volume work that actually needs judgment — writing the digest that matters — escalates to a cloud model. *When local quality suffices vs. when it's worth paying for cloud* becomes real, measurable engineering, not a toggle. You're also never blocked by API cost or rate limits while learning, and you end up with something you'll actually keep using — it's built to help you find the next thing worth adding to this very notebook.

**Local-first stack on your Mac:**

| Your Mac's RAM | Model to pull first |
|---|---|
| 16GB | `ollama pull phi4` |
| 36GB | `ollama pull llama3.3:8b` or `qwen3:14b` |
| 64GB | `ollama pull qwen3:34b` |
| 128GB | `ollama pull llama3.3:70b` |

Ollama (0.19+) runs Apple's MLX backend natively on Apple Silicon by default — install it, pull whatever row matches your machine, and you have a local, OpenAI-compatible endpoint running before Week 1 is over.

**The swap-to-cloud requirement, solved once, used everywhere:** build one thin interface — `generate(prompt, tier="local"|"cloud")` — where `local` hits Ollama's endpoint and `cloud` hits Bedrock/Anthropic. Every module below calls that interface, never a specific provider directly. Get this right in Week 1 and "still works on a cloud API" is free for the rest of the notebook.

If you'd rather point this whole sequence at a different local-first project, swap it — the module order underneath doesn't change.

---

## Month 1 — Foundations & Core RAG (Weeks 1–4)

### Week 1 — LLM Foundations
- [x] Transformer architecture at a working level: attention, tokens, context windows **(review)**
- [x] Prompting patterns: zero-shot, few-shot, chain-of-thought, structured output prompting
- [x] Model selection tradeoffs: latency, cost, context length, reasoning vs. speed models
- [x] Chat vs. completion APIs, streaming, function/tool-calling basics **(review)**
- [x] **Scout:** install Ollama, pull your tier's model, build the `generate(prompt, tier)` interface, sketch Scout's full architecture end-to-end

### Week 2 — Embeddings
- [x] What an embedding is: dense vectors, dimensionality, semantic space
- [x] Dense vs. sparse embeddings (BM25/SPLADE vs. OpenAI/Cohere/Titan embeddings)
- [x] Similarity metrics: cosine similarity, dot product, Euclidean — when each matters
- [x] Bi-encoders vs. cross-encoders (resurfaces at reranking — learn it now)
- [x] **Scout:** pull a local embedding model (e.g. `nomic-embed-text`) and embed your first batch of 30–50 arXiv abstracts + blog posts — embeddings are high-volume enough that they should basically always run local

### Week 3 — Vector Databases
- [x] Indexing algorithms: HNSW, IVF — why they trade exactness for speed
- [x] Compare Chroma, pgvector, Weaviate, Pinecone, AWS OpenSearch/S3 Vectors, Bedrock Knowledge Bases **(you know Bedrock KBs — benchmark it against the fully-local options)**
- [x] Metadata filtering and hybrid schemas (vector + structured fields)
- [x] **Scout:** stand up a local vector store (Chroma or pgvector — no cloud dependency) and load the Week 2 embeddings into it

### Week 4 — Naive RAG, Built by Hand
- [x] Chunking strategies: fixed-size, recursive, semantic, document-aware
- [x] Full naive pipeline: chunk → embed → store → retrieve → stuff into prompt → generate
- [x] Where naive RAG breaks: lost context at chunk boundaries, irrelevant retrieval, stale data
- [x] **Scout v0.1:** naive RAG.

---

## Month 2 — Advanced RAG & Knowledge Bases (Weeks 5–8)

### Week 5 — Hybrid Search & Reranking
- [ ] Hybrid retrieval: combining keyword (BM25) and vector search
- [ ] Reciprocal Rank Fusion (RRF) for merging result sets
- [ ] Reranking with cross-encoders (Cohere Rerank, BGE-Reranker, ColBERT late-interaction)
- [ ] **Scout v0.2:** add hybrid search + a local reranker (BGE-Reranker runs fine via `sentence-transformers` on Apple Silicon) — measure the precision lift over v0.1

### Week 6 — Query Transformation
- [ ] Query rewriting and decomposition for multi-hop questions (RQ-RAG pattern)
- [ ] HyDE (Hypothetical Document Embeddings)
- [ ] Conversational query rewriting for multi-turn RAG (resolving "it," "that," follow-ups)
- [ ] **Scout:** first real local-vs-cloud quality test — run query rewriting on `tier="local"` vs `tier="cloud"` on the same 10 queries and actually compare the outputs side by side

### Week 7 — Advanced RAG Architectures
- [ ] Contextual retrieval — prepend chunk-level context before embedding; meaningfully cuts retrieval failures
- [ ] GraphRAG — knowledge graphs from documents for relationship/multi-hop queries
- [ ] RAPTOR — hierarchical summarization for long documents
- [ ] Agentic RAG — agent decides whether to re-retrieve, instead of retrieving once
- [ ] Self-RAG / Adaptive RAG — self-critique and conditional retrieval
- [ ] **Scout:** contextual retrieval on paper/blog chunks; GraphRAG to map paper ↔ technique ↔ framework relationships; RAPTOR to summarize long threads/papers

### Week 8 — Knowledge Base Design
- [ ] Structured vs. unstructured KB design, metadata schema design
- [ ] Freshness/sync strategies — keeping a KB current against a moving source of truth
- [ ] Access control and multi-tenant KB patterns (directly relevant to client-embedded work)
- [ ] **Scout:** formalize the KB — arXiv feed, blog RSS, source metadata, and a real freshness policy (papers and posts never stop arriving; dedup matters here)

---

## Month 3 — Memory, Context Engineering & Tool Use (Weeks 9–12)

### Week 9 — Context Engineering
- [ ] Context engineering vs. prompt engineering — the field-level distinction (treated as *the* core 2026 AI engineering skill)
- [ ] The four moves: write, select, compress, isolate
- [ ] Context window budgeting for multi-step agents
- [ ] Anti-patterns: context poisoning, context overload, stale context
- [ ] **Scout:** design exactly what goes into the "write the digest" prompt — this is the one call worth spending cloud-tier budget on, so get the context tight

### Week 10 — Memory Systems
- [ ] Short-term memory: conversation buffers, sliding windows, summarization-on-overflow
- [ ] Long-term memory: episodic (what happened) vs. semantic (facts/preferences learned)
- [ ] Memory frameworks: Mem0, Letta (OS-inspired context paging), LangGraph's built-in memory, Bedrock AgentCore Memory
- [ ] Write policy design — deciding *when* something is worth remembering, not just how to store it
- [ ] **Scout:** memory for what's already been seen (no repeat surfacing) and which topics you actually engage with over time — this should get sharper the longer you run it

### Week 11 — Tool Use & MCP
- [ ] Function/tool calling mechanics, tool schema design, structured output validation **(review)**
- [ ] MCP (Model Context Protocol) fundamentals — client/server/host architecture
- [ ] Build a minimal MCP server exposing one real tool
- [ ] MCP security basics: sandboxing, scoped auth per server, least-privilege tool access
- [ ] **Scout:** build it an MCP server — arXiv search, blog/RSS fetching, as real callable tools instead of hardcoded fetch calls

### Week 12 — Multi-Agent Coordination
- [ ] A2A (Agent-to-Agent) protocol — how it differs from MCP (tool access vs. agent-to-agent negotiation)
- [ ] Handoff patterns vs. supervisor/worker patterns vs. peer negotiation
- [ ] When multi-agent actually helps vs. when it's just overhead (most tasks don't need it)
- [ ] **Scout:** split into sub-agents — a scout (finds new content), a synthesizer (writes the digest), a curator (decides what's actually worth a human's time)

---

## Month 4 — Agent Architectures & Evaluation (Weeks 13–16)

### Week 13 — Deepen LangGraph
- [ ] ReAct pattern from first principles **(review)**
- [ ] State machines, checkpointing, durable execution **(review — go deeper: crash recovery, human-in-the-loop interrupts)**
- [ ] Persistent checkpointers (e.g. Postgres-backed) for production state
- [ ] **Scout:** rebuild the orchestration as a LangGraph state machine where the local-vs-cloud choice is a real conditional edge — the curator's confidence score decides which model tier writes the final output

### Week 14 — Compare the Field
- [ ] CrewAI — role-based multi-agent, fastest to prototype, strongest current MCP support
- [ ] OpenAI Agents SDK — handoff model, guardrails in under 100 lines, OpenAI-model-centric
- [ ] Claude Agent SDK — MCP-native, lifecycle hooks, in-process server model
- [ ] **Scout:** rebuild just the scout sub-agent in CrewAI (or another framework) — feel the tradeoff against LangGraph directly, on a piece you already have working

### Week 15 — Evaluation
- [ ] Golden datasets — building a test set that actually represents production traffic
- [ ] LLM-as-judge patterns and their failure modes (self-preference bias, inconsistency)
- [ ] Behavioral regression testing — catching "it got worse" before users do
- [ ] **Scout:** build a golden set of "should this have been surfaced?" judgments, and specifically measure where the local model's triage disagrees with a cloud judge — that gap is the real answer to "how good is good enough locally"

### Week 16 — Observability & Guardrails
- [ ] Tracing every step: LLM calls, tool calls, retrieval, decisions (LangSmith or Langfuse)
- [ ] Input/output guardrails: prompt injection defense, PII handling, output validation
- [ ] Permission scoping and audit trails for regulated environments **(you have a real head start here via HCA)**
- [ ] **Scout:** trace every local-vs-cloud routing decision with the reason it was made, and add a running $ counter for cloud calls — you can now show, in real numbers, what the local-first split is actually saving

---

## Month 5 — Production, Fine-Tuning & Capstone (Weeks 17–22)

### Week 17 — Fine-Tuning Fundamentals
- [ ] When to fine-tune vs. when RAG/prompting is enough (usually: exhaust the others first)
- [ ] LoRA / QLoRA — parameter-efficient fine-tuning, why it's the default now
- [ ] A conceptual pass on RLHF/DPO — understand what it does, no need to implement it
- [ ] **Scout (stretch):** fine-tune your local model specifically on "is this paper actually novel/relevant" — high-volume, well-defined, exactly the task small local models are good for

### Week 18 — Deployment Infrastructure
- [ ] Containerizing an agent (Docker)
- [ ] Infrastructure-as-code for agents: CDK/Terraform
- [ ] Bedrock AgentCore Runtime, Gateway, Identity — deploy the cloud-tier half here, given your AWS background
- [ ] Prompt caching and semantic caching for cost/latency
- [ ] **Scout:** real hybrid deployment — cloud-tier calls run through AgentCore, local-tier stays on your Mac; harden the `generate()` interface so a dead Ollama process fails over to cloud instead of crashing the run

### Week 19 — Security & Governance
- [ ] Prompt injection and jailbreak defense patterns
- [ ] Data privacy in regulated workflows — audit trails, explainability, least-agency design
- [ ] Cost/token economics at production scale
- [ ] **Scout:** treat "runs local by default" as the privacy control it actually is, and lock down cloud API keys / scoped credentials for the escalation path

### Weeks 20–22 — Harden & Present
- [ ] Stress-test Scout: a source that goes down, a malformed feed, a week with 10x the normal volume
- [ ] Write it up as a case study — architecture, the local/cloud routing decisions and why, what broke and how you fixed it — this is the artifact you walk an FDE interviewer through
- [ ] Keep it running — the best proof this works is it still finding things worth reading in January
- [ ] Buffer — nothing above ever fits the box exactly. Catch up here.

---

## Scratch Space / Your Own Notes
*(leave this for terms, gotchas, and links you want to find again fast)*

