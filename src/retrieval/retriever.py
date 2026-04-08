import requests
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.embedding_utils import create_embeddings
from src.utils.config import EMBEDDINGS_FILE







def load_embeddings():
    """
    Load precomputed embeddings dataframe
    """
    try:
        df = joblib.load(EMBEDDINGS_FILE)
        return df
    except Exception as e:
        raise Exception(f"Failed to load embeddings: {e}")


def retrieve(query, top_k=5):
    """
    Retrieve top_k most relevant chunks for a query
    """

    df = load_embeddings()

    if df.empty:
        raise Exception("Embeddings dataframe is empty")

    # Create query embedding
    query_embedding = create_embeddings([query])[0]

    # Compute similarity
    similarities = cosine_similarity(
        np.vstack(df["embedding"]),
        [query_embedding]
    ).flatten()

    # Get top indices
    top_indices = similarities.argsort()[::-1][:top_k]

    # IMPORTANT: use iloc (not loc)
    results = df.iloc[top_indices].copy()
    scores = similarities[top_indices]

    # Attach scores (very useful for explainability)
    results["score"] = scores

    return results