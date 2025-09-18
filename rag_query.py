from sentence_transformers import SentenceTransformer
import chromadb

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Get the documents collection
collection = client.get_collection(name="documents_collection")

def query_documents(query_text, n_results=3):
    """
    Query the document collection and return the most similar documents.
    """
    # Embed the query
    query_embedding = model.encode([query_text]).tolist()

    # Search for similar documents
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results,
        include=['metadatas', 'distances']
    )

    return results

def demo_rag():
    """
    Demonstrate the RAG system with sample queries.
    """
    sample_queries = [
        "What is retrieval-augmented generation?",
        "How do embeddings help in search?",
        "Tell me about vector databases",
        "Why use local models for embeddings?"
    ]

    for query in sample_queries:
        print(f"\nQuery: {query}")
        print("-" * 50)

        results = query_documents(query)

        for i, (id, metadata, distance) in enumerate(zip(results['ids'][0], results['metadatas'][0], results['distances'][0])):
            print(f"Result {i+1}:")
            print(f"Title: {metadata['title']}")
            print(f"Content: {metadata['content']}")
            print(f"Similarity Score: {1 - distance:.4f}")  # Convert distance to similarity
            print("-" * 30)

if __name__ == "__main__":
    demo_rag()
