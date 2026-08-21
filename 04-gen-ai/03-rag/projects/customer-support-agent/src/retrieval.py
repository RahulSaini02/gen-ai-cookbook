"""Vector database retrieval and formatting."""

import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)
from config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_DB_PATH,
    DEFAULT_DISTANCE_THRESHOLD,
    DEFAULT_TOP_K,
    EMBEDDING_MODEL,
    OLLAMA_URL,
)


def get_collection():
    """Get or create ChromaDB collection."""
    ollama_ef = OllamaEmbeddingFunction(
        url=OLLAMA_URL,
        model_name=EMBEDDING_MODEL,
    )

    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = client.get_or_create_collection(
        CHROMA_COLLECTION_NAME,
        embedding_function=ollama_ef,
    )

    if collection is None:
        raise ValueError(
            f"Failed to get or create collection: {CHROMA_COLLECTION_NAME}"
        )

    return collection


def query_research(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    distance_threshold: float = DEFAULT_DISTANCE_THRESHOLD,
) -> list[dict]:
    """Query vector DB and return relevant chunks."""
    collection = get_collection()
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    output = []
    documents = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    for i in range(len(documents)):
        result = {
            "document": documents[i],
            "distance": distances[i],
            "metadata": metadatas[i],
        }

        if result["distance"] <= distance_threshold:
            output.append(result)

    return output[:top_k]


def format_context(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    threshold: float = DEFAULT_DISTANCE_THRESHOLD,
) -> str:
    """Retrieve chunks and format as context for Scout agent."""
    results = query_research(query, top_k, threshold)

    if not results:
        return "No relevant information available"

    context = ""
    for i, result in enumerate(results, 1):
        context += f"[Source: {result['metadata']['file_name']}, page {result['metadata']['page_num']}]\n"
        context += result["document"] + "\n\n"

    return context
