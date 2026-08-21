"""Setup script to initialize ChromaDB with embeddings."""

import json
from pathlib import Path

from chromadb.errors import ChromaError
from config import DOCS_DIR, EMBEDDINGS_FILE
from src.embeddings import generate_embeddings
from src.retrieval import get_collection


def setup_database():
    """Load embeddings into ChromaDB."""
    try:
        file_path = Path(EMBEDDINGS_FILE)

        if file_path.exists() == False:
            print(
                f"Embeddings file not found: {EMBEDDINGS_FILE}. Running generate_embeddings() first."
            )
            embeddings = generate_embeddings(
                library=Path(DOCS_DIR), chunk_size=100, overlap=0.70
            )
            with open(EMBEDDINGS_FILE, "w", encoding="utf-8") as file:
                json.dump(embeddings, file, indent=4)

        with open(EMBEDDINGS_FILE, "r") as f:
            all_chunks = json.load(f)
        print(f"Found {len(all_chunks)} chunks")

        print("Initializing ChromaDB...")
        collection = get_collection()

        print("Adding embeddings to database...")
        collection.add(
            ids=[chunk["id"] for chunk in all_chunks],
            documents=[chunk["text"] for chunk in all_chunks],
            embeddings=[chunk["embeddings"] for chunk in all_chunks],
            metadatas=[chunk["metadata"] for chunk in all_chunks],
        )

        print(f"✓ Database initialized with {len(all_chunks)} chunks")

    # Catch issues specifically related to ChromaDB operations
    except ChromaError as e:
        print(f"✕ ChromaDB database error occurred: {e}")
        return
    # Catch file-related errors
    except (FileNotFoundError, OSError, json.JSONDecodeError) as e:
        print(f"✕ Unexpected error initializing database: {e}")
        return


if __name__ == "__main__":
    setup_database()
