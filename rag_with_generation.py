from sentence_transformers import SentenceTransformer
import chromadb
import ollama

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Get the documents collection
collection = client.get_collection(name="documents_collection")

def retrieve_documents(query_text, n_results=3):
    """
    Retrieve the most similar documents for a query.
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

def generate_answer(query, retrieved_docs):
    """
    Generate an answer using Ollama based on the query and retrieved documents.
    """
    # Construct the context from retrieved documents
    context = "\n\n".join([
        f"Document {i+1}: {doc['title']}\n{doc['content']}"
        for i, doc in enumerate(retrieved_docs)
    ])

    # Create the prompt
    prompt = f"""You are a helpful assistant. Use the following context to answer the question accurately.
If the context doesn't contain enough information, say so.

Context:
{context}

Question: {query}

Answer:"""

    try:
        # Generate response using Ollama (using tinyllama model)
        response = ollama.generate(
            model='tinyllama',  # Using tinyllama model
            prompt=prompt,
            options={
                'temperature': 0.1,  # Low temperature for consistent answers
                'num_predict': 200   # Limit response length
            }
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error generating response: {str(e)}. Make sure Ollama is running with 'tinyllama' model."

def rag_pipeline(query):
    """
    Complete RAG pipeline: retrieve + generate
    """
    print(f"Query: {query}")
    print("=" * 60)

    # Step 1: Retrieve relevant documents
    results = retrieve_documents(query)

    retrieved_docs = []
    print("Retrieved Documents:")
    for i, (id, metadata, distance) in enumerate(zip(results['ids'][0], results['metadatas'][0], results['distances'][0])):
        similarity = 1 - (distance / 2)  # Proper cosine similarity conversion
        print(f"{i+1}. {metadata['title']} (Similarity: {similarity:.3f})")
        print(f"   {metadata['content'][:100]}...")
        retrieved_docs.append(metadata)
        print()

    # Step 2: Generate answer
    print("Generated Answer:")
    print("-" * 30)
    answer = generate_answer(query, retrieved_docs)
    print(answer)
    print()

def demo_rag_with_generation():
    """
    Demonstrate the complete RAG pipeline with generation.
    """
    sample_queries = [
        "What is RAG and how does it work?",
        "Explain the benefits of using local embeddings",
        "How do vector databases help with AI applications?"
    ]

    for query in sample_queries:
        rag_pipeline(query)
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    demo_rag_with_generation()
