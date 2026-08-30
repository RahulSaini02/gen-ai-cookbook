"""Configuration for customer support agent."""

# Ollama settings
OLLAMA_URL = "http://localhost:11434"
OLLAMA_TIMEOUT = 2

# Embedding settings
EMBEDDING_MODEL = "embeddinggemma"
EMBEDDING_DIM = 768

# Chunking settings
DEFAULT_CHUNK_SIZE = 200
DEFAULT_OVERLAP = 0.5

# Retrieval settings (ChromaDB uses Euclidean distance)
DEFAULT_TOP_K = 5
DEFAULT_DISTANCE_THRESHOLD = 1.5

# ChromaDB settings
CHROMA_DB_PATH = "./data/chroma_db"
CHROMA_COLLECTION_NAME = "customer-support-agent"

# Database settings
DATABASE_PATH = "./data/support.db"

# Data paths
DATA_DIR = "./data"
DOCS_DIR = "./data/docs"
EMBEDDINGS_DIR = "./data/embeddings"
EMBEDDINGS_FILE = "./data/embeddings/data.json"
PROMPTS_DIR = "./prompts"

# LLM settings
DEFAULT_LLM_MODEL = "gemma4"
DEFAULT_LLM_TIER = "cloud"
