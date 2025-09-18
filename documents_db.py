# Simple text-based database of documents for RAG demo

documents = [
    {
        "id": "doc_1",
        "title": "What is RAG?",
        "content": "RAG stands for Retrieval-Augmented Generation. It combines retrieval of relevant information from a knowledge base with generative AI to provide more accurate and context-aware responses."
    },
    {
        "id": "doc_2",
        "title": "How does vector search work?",
        "content": "Vector search works by converting text into numerical vectors using embedding models. These vectors capture semantic meaning, allowing similarity searches based on meaning rather than exact keyword matches."
    },
    {
        "id": "doc_3",
        "title": "What is ChromaDB?",
        "content": "ChromaDB is an open-source vector database designed for storing and retrieving embeddings. It supports efficient similarity search and is optimized for AI applications."
    },
    {
        "id": "doc_4",
        "title": "Benefits of local embeddings",
        "content": "Local embeddings provide privacy by keeping data on-premise, reduce API costs, and offer better control over the embedding model. They work offline and can be customized for specific domains."
    },
    {
        "id": "doc_5",
        "title": "Sentence Transformers",
        "content": "Sentence Transformers is a Python library for computing dense vector representations of sentences, texts, and images. It provides pre-trained models that can be used locally without API calls."
    }
]

def get_documents():
    return documents
