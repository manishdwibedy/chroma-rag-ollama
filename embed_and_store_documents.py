from sentence_transformers import SentenceTransformer
import chromadb
from documents_db import get_documents

# Load the OSS model (runs locally, no API)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Get documents from the simple text-based DB
documents = get_documents()

# Extract texts to embed
texts = [doc['content'] for doc in documents]

# Generate embeddings
embeddings = model.encode(texts)

# Initialize ChromaDB client (local, persistent)
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get a collection for documents
collection = client.get_or_create_collection(name="documents_collection")

# Add embeddings to the collection with metadata
collection.add(
    embeddings=embeddings.tolist(),
    metadatas=[{"title": doc['title'], "content": doc['content']} for doc in documents],
    ids=[doc['id'] for doc in documents]
)

print("Document embeddings generated and stored in ChromaDB.")
