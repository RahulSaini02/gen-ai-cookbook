#  Important Components of LangChain

## 🧠 1. RAG: Retrieval Augmented Generation

RAG enhances language model outputs by injecting retrieved context from an external source (e.g., documents) into the prompt.

### Data Ingestion Flow

#### Data Sources
Supported formats: PDFs, Websites, APIs, JSON, URLs

LangChain loads these inputs as raw data.

#### Data Transformation
- **Split:** Raw data ➝ Text ➝ Chunks

- **Embed:** Chunks ➝ Embeddings (Numerical Vectors)

- **Store:** Embedded vectors stored in a VectorStore DB

#### Embedding and Vector Database
- Text ➝ Vector Embeddings
Each chunk of text is transformed into vectors via embedding models.

- **VectorStore DB Options:**
  - FAISS

  - ChromaDB

  - AstraDB

#### Query Flow (During Retrieval)
Query is embedded into a vector.

Similarity Search is performed in the VectorStore DB.

Relevant context (nearest vectors) is retrieved.

This context is sent along with the original query to the LLM.

#### LLM Integration
The retrieved Context + Prompt is processed by the LLM.

Output is generated based on the limited context window of the model.

> ⚠️ Note: LLMs have context length limitations.

#### Retrieval Chain Workflow
> User Question ➝ Retrieve relevant context from VectorStore DB ➝ Compose Prompt + Context Info ➝ Feed to LLM ➝ Receive final Answer/Output (Response)

This forms the "Retrieval Chain" in LangChain.

## Interface Summary
**LangChain Interface handles:**

1. Data loading

2. Text chunking

3. Embedding

4. Storage

5. Retrieval

6. LLM communication