import requests
import os
import json
import pandas as pd
import joblib

# from src.embeddings.retriever import create_embeddings  # or utils later
# (If circular import, we’ll move it to utils next step)


TRANSCRIPTS_DIR = "data/transcripts"
OUTPUT_PATH = "data/embeddings.joblib"
EMBED_API_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "bge-m3"
from src.utils.embedding_utils import create_embeddings



def load_transcripts():
    """
    Load all transcript JSON files and return chunk list
    """
    all_chunks = []

    for file in os.listdir(TRANSCRIPTS_DIR):
        if not file.endswith(".json"):
            continue

        with open(os.path.join(TRANSCRIPTS_DIR, file), "r") as f:
            content = json.load(f)

        all_chunks.extend(content["chunks"])

    return all_chunks


def build_embeddings():
    """
    Generate embeddings for all transcript chunks and save them
    """
    chunks = load_transcripts()

    print(f"Loaded {len(chunks)} chunks")
    if len(chunks) == 0:
        raise Exception("No transcript chunks found in data/transcripts")
    texts = [chunk["text"] for chunk in chunks]

    embeddings = create_embeddings(texts)

    records = []
    for i, chunk in enumerate(chunks):
        records.append({
            "chunk_id": i,
            "title": chunk["title"],
            "number": chunk["number"],
            "start": chunk["start"],
            "end": chunk["end"],
            "text": chunk["text"]strip(),
            "embedding": embeddings[i]
        })

    df = pd.DataFrame(records)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    joblib.dump(df, OUTPUT_PATH)

    print(f"Saved embeddings to {OUTPUT_PATH}")