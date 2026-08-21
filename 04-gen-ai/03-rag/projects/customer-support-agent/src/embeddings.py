from pathlib import Path

import ollama
import pymupdf
from config import DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP, EMBEDDING_MODEL
from ollama import ResponseError

from src.llm import is_ollama_active


def load_pdf(file_path: Path, test_pages: int | None = None) -> list[dict]:
    """Load PDF pages and return their text with metadata."""
    pdf_content = []
    file_name = file_path.stem

    with pymupdf.open(file_path) as doc:
        pages = (
            range(len(doc)) if test_pages is None else range(min(test_pages, len(doc)))
        )

        for page_num in pages:
            page = doc.load_page(page_num)
            pdf_content.append(
                {
                    "file_name": file_name,
                    "page_num": page_num + 1,
                    "page_content": page.get_text(),
                }
            )

    return pdf_content


def load_text_file(file_path: Path) -> list[dict]:
    """Load text/markdown file and return content as single page."""
    file_name = file_path.stem
    content = file_path.read_text(encoding="utf-8")

    return [
        {
            "file_name": file_name,
            "page_num": 1,
            "page_content": content,
        }
    ]


def load_document(file_path: Path, test_pages: int | None = None) -> list[dict]:
    """Load document (PDF or text) and return content with metadata."""
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf(file_path, test_pages)
    elif suffix in [".md", ".txt"]:
        return load_text_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}. Supported: .pdf, .md, .txt")


# Chunk Text
def chunk_text(text: str, chunk_size: int = 200, overlap: float = 0.5) -> list[str]:

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if not 0 <= overlap < 1:
        raise ValueError("overlap must be between 0 and 1")

    if not text or not text.strip():
        return []

    words = text.split()
    step = max(1, int(chunk_size * (1 - overlap)))

    chunks = []

    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + chunk_size])
        chunks.append(chunk)

    return chunks


def chunk_doc(text: str) -> list[str]:
    """Split documentation into ## sections."""

    if not text or not text.strip():
        return []

    chunks = []
    current_section = []

    for line in text.splitlines():
        # Detect a new ## section
        if line.startswith("## ") and not line.startswith("### "):
            # Save previous section
            if current_section:
                chunks.append("\n".join(current_section))

            # Start new section
            current_section = [line]

        else:
            current_section.append(line)

    # Don't forget the final section
    if current_section:
        chunks.append("\n".join(current_section))

    return chunks


# Embed Text
def embed(text: str, model: str = EMBEDDING_MODEL) -> list[float]:
    """Embed text using Ollama embedding model."""
    if not is_ollama_active():
        return []

    try:
        response = ollama.embed(model=model, input=text)
        return response.embeddings[0]
    except ResponseError as e:
        print(f"Embedding error: {e}")
        return []


def generate_embeddings(
    library: Path,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: float = DEFAULT_OVERLAP,
) -> list[dict]:
    """Generate embeddings for all documents (PDF, MD, TXT) in a library."""
    embeddings = []
    supported_formats = {".pdf", ".md", ".txt"}

    for item in library.iterdir():
        if item.suffix.lower() not in supported_formats:
            continue

        print(f"Processing {item.name}...")
        try:
            content = load_document(item)
        except ValueError as e:
            print(f"  Skipping: {e}")
            continue

        suffix = item.suffix.lower()

        if suffix == ".pdf":
            for page in content:
                chunks = chunk_text(page["page_content"], chunk_size, overlap)

                for chunk_idx, chunk_text_content in enumerate(chunks):
                    vec = embed(chunk_text_content)

                    if not vec:
                        continue

                    data = {
                        "id": f"{page['file_name']}_page{page['page_num']}_chunk{chunk_idx}",
                        "text": chunk_text_content,
                        "embeddings": vec,
                        "metadata": {
                            "file_name": page["file_name"],
                            "page_num": page["page_num"],
                            "chunk_index": chunk_idx,
                        },
                    }
                    embeddings.append(data)

        else:
            text_content = content[0]["page_content"]
            chunks = chunk_doc(text_content)

            for chunk_idx, chunk_text_content in enumerate(chunks):
                vec = embed(chunk_text_content)

                if not vec:
                    continue

                data = {
                    "id": f"{item.stem}_page{content[0]['page_num']}_chunk{chunk_idx}",
                    "text": chunk_text_content,
                    "embeddings": vec,
                    "metadata": {
                        "file_name": item.stem,
                        "page_num": content[0]["page_num"],
                        "chunk_index": chunk_idx,
                    },
                }
                embeddings.append(data)

    return embeddings
