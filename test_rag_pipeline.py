import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag_with_generation import retrieve_documents, generate_answer, rag_pipeline

def test_retrieval():
    print("Testing retrieval...")
    query = "What is RAG?"
    results = retrieve_documents(query)
    if results['ids']:
        print(f"Retrieved {len(results['ids'][0])} documents for query: {query}")
        for i, (id, metadata) in enumerate(zip(results['ids'][0], results['metadatas'][0])):
            print(f"{i+1}. {metadata['title']}")
    else:
        print("No documents retrieved.")
    print()

def test_generation():
    print("Testing generation...")
    query = "Explain vector databases."
    # Mock retrieved docs
    retrieved_docs = [
        {"title": "What is ChromaDB?", "content": "ChromaDB is an open-source vector database..."},
        {"title": "How does vector search work?", "content": "Vector search works by converting text..."}
    ]
    answer = generate_answer(query, retrieved_docs)
    print(f"Generated answer: {answer[:100]}...")
    print()

def test_edge_cases():
    print("Testing edge cases...")
    # Empty query
    try:
        results = retrieve_documents("")
        print("Empty query handled.")
    except Exception as e:
        print(f"Empty query error: {e}")

    # Long query
    long_query = "This is a very long query to test how the system handles extremely long input text that might exceed normal limits and see if it can still retrieve relevant documents or generate a response without crashing or producing irrelevant results. " * 10
    results = retrieve_documents(long_query)
    print(f"Long query retrieved {len(results['ids'][0])} documents.")

    # Query with no matches
    no_match_query = "This query has no matching documents in the database."
    results = retrieve_documents(no_match_query)
    print(f"No match query retrieved {len(results['ids'][0])} documents.")
    print()

def test_full_pipeline():
    print("Testing full pipeline...")
    test_queries = [
        "What is RAG?",
        "Benefits of local embeddings",
        "Vector databases in AI"
    ]
    for query in test_queries:
        print(f"Testing query: {query}")
        rag_pipeline(query)
        print("-" * 50)

if __name__ == "__main__":
    test_retrieval()
    test_generation()
    test_edge_cases()
    test_full_pipeline()
    print("Thorough testing completed.")
