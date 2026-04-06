import os
from src.retrieval.retriever import retrieve
from src.generation.generator import generate_answer
from src.embeddings.embedder import build_embeddings

def main():
    print("🎥 Video RAG System")
    print("--------------------")

    query = input("Ask a question: ").strip()

    if not query:
        print("Please enter a valid question.")
        return

    try:
        

        if not os.path.exists("data/embeddings.joblib"):
            print("Embeddings not found. Building...")
            build_embeddings()

        # Step 1: Retrieve relevant chunks
        results = retrieve(query, top_k=5)

        # Step 2: Generate answer
        answer = generate_answer(query, results)

        print("\n=== ANSWER ===\n")
        print(answer)

        print("\n=== SOURCES ===\n")
        for i, (_, row) in enumerate(results.iterrows()):
            print(f"{i+1}. {row['title']} (#{row['number']}) "
                  f"[{row['start']}s - {row['end']}s] "
                  f"(score: {row['score']:.3f})")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    

    main()