import requests

LLM_API_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "llama3.2"


def build_prompt(query, results):
    """
    Build structured prompt using retrieved chunks
    """

    context = ""

    for i, (_, row) in enumerate(results.iterrows()):
        context += f"""
[Rank {i+1} | Score: {row['score']:.3f}]
Video: {row['title']} (#{row['number']})
Time: {row['start']} - {row['end']}
Text: {row['text'][:300]}
---
"""

    prompt = f"""
You are helping a student navigate lecture videos.

Context:
{context}

Question:
{query}

Instructions:
- Mention the video name
- Mention exact timestamps
- Explain briefly and clearly
- Guide the user to where to watch

Answer:
"""

    return prompt


def generate_answer(query, results):
    """
    Generate answer using LLM
    """

    prompt = build_prompt(query, results)

    try:
        response = requests.post(
            LLM_API_URL,
            json={
                "model": LLM_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code != 200:
            raise Exception(f"LLM API Error: {response.text}")

        data = response.json()

        if "response" not in data:
            raise Exception("Invalid LLM response format")

        return data["response"]

    except Exception as e:
        print(f"Generation error: {e}")
        raise