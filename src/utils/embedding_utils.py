import requests

EMBED_API_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "bge-m3"


def create_embeddings(text_list, batch_size=32):
    """
    Generate embeddings using local embedding API
    """

    all_embeddings = []

    for i in range(0, len(text_list), batch_size):
        batch = text_list[i:i + batch_size]

        try:
            response = requests.post(
                EMBED_API_URL,
                json={
                    "model": EMBED_MODEL,
                    "input": batch
                },
                timeout=30
            )

            if response.status_code != 200:
                raise Exception(f"API Error: {response.text}")

            data = response.json()

            if "embeddings" not in data:
                raise Exception("Invalid response format")

            all_embeddings.extend(data["embeddings"])

        except Exception as e:
            print(f"Embedding error: {e}")
            raise

    return all_embeddings


