import chromadb

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Get the collection
collection = client.get_collection(name="sample_embeddings")

# Query all items in the collection
results = collection.get(include=['metadatas', 'embeddings'])

print("Results keys:", results.keys())
print("IDs:", results.get('ids'))
print("Metadatas:", results.get('metadatas'))
print("Embeddings:", results.get('embeddings') is not None)

if results['ids']:
    print("Stored embeddings:")
    for i, id in enumerate(results['ids']):
        metadata = results['metadatas'][i] if results['metadatas'] else None
        embedding = results['embeddings'][i] if results['embeddings'] is not None else None
        print(f"ID: {id}")
        print(f"Text: {metadata['text'] if metadata else 'N/A'}")
        print(f"Embedding shape: {len(embedding) if embedding is not None else 'N/A'}")
        print("---")

    print(f"Total embeddings stored: {len(results['ids'])}")
else:
    print("No embeddings found in the collection.")
