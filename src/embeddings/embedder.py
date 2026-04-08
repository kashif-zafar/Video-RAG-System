import requests
import os
import json
import pandas as pd
import joblib
from src.utils.config import TRANSCRIPT_DIR, EMBEDDINGS_FILE
# then use TRANSCRIPT_DIR and EMBEDDINGS_FILE instead of the hardcoded strings




from src.utils.embedding_utils import create_embeddings



def load_transcripts():
    """
    Load all transcript JSON files and return chunk list
    """
    all_chunks = []

    for file in os.listdir(TRANSCRIPT_DIR):
        if not file.endswith(".json"):
            continue

        with open(os.path.join(TRANSCRIPT_DIR, file), "r") as f:
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
            "text": chunk["text"].strip(),
            "embedding": embeddings[i]
        })

    df = pd.DataFrame(records)

    os.makedirs(os.path.dirname(EMBEDDINGS_FILE), exist_ok=True)
    joblib.dump(df, EMBEDDINGS_FILE)

    print(f"Saved embeddings to {EMBEDDINGS_FILE}")