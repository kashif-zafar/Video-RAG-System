"""Configuration module."""

# Model configurations
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384

# File paths
DATA_DIR = "data/"
VIDEO_DIR = "data/videos/"
AUDIO_DIR = "data/audios/"
TRANSCRIPT_DIR = "data/transcripts/"
EMBEDDINGS_FILE = "data/embeddings.joblib"

# Processing parameters
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50
SIMILARITY_THRESHOLD = 0.5
