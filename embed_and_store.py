from sentence_transformers import SentenceTransformer
import chromadb

# Load the OSS model (runs locally, no API)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample texts to embed
texts = [
    "This is a sample sentence for embedding.",
    "Another example text to demonstrate vector storage.",
    "Open-source models are great for local processing."
]

# Generate embeddings
embeddings = model.encode(texts)

# Initialize ChromaDB client (local, persistent)
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get a collection
collection = client.get_or_create_collection(name="sample_embeddings")

# Add embeddings to the collection
collection.add(
    embeddings=embeddings.tolist(),
    metadatas=[{"text": text} for text in texts],
    ids=[f"id_{i}" for i in range(len(texts))]
)

print("Embeddings generated and stored in local ChromaDB.")
