# RAG System with Local Embeddings and Vector Database

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project implements a Retrieval-Augmented Generation (RAG) system using open-source models for embeddings and a local vector database. It allows you to store documents, retrieve relevant information based on queries, and generate answers using a local language model via Ollama.

## Use Case

This system is ideal for:
- Building a local knowledge base or Q&A system
- Answering questions based on a collection of documents
- Implementing privacy-preserving AI applications without relying on external APIs
- Educational or research purposes where data stays on-premise

## Features

- **Local Embeddings**: Uses Sentence Transformers (all-MiniLM-L6-v2) for generating embeddings without API calls
- **Vector Database**: Stores embeddings in ChromaDB, a local vector database
- **Document Retrieval**: Efficient similarity search for relevant documents
- **Answer Generation**: Uses Ollama with tinyllama model for generating context-aware answers
- **Modular Design**: Separate scripts for embedding, storing, querying, and generation
- **Testing Suite**: Comprehensive tests for the RAG pipeline

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running (for text generation)
- Git (for cloning if needed)

## Installation and Setup

### 1. Clone or Download the Project

If using git:
```bash
git clone <repository-url>
cd rag-system
```

### 2. Set Up Virtual Environment

Run the setup script to create a virtual environment and install dependencies:

```bash
chmod +x setup_env.sh
./setup_env.sh
```

This will:
- Create a Python virtual environment in `venv/`
- Activate the environment
- Upgrade pip
- Install required packages from `requirements.txt`

### 3. Activate Virtual Environment (if not using the script)

If you didn't run the setup script, activate the environment manually:

```bash
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 4. Install Ollama and Pull Model

Install Ollama from [ollama.ai](https://ollama.ai) if not already installed.

Pull the tinyllama model:

```bash
ollama pull tinyllama
```

Start Ollama server:

```bash
ollama serve
```

### 5. Prepare Documents

The system comes with sample documents. To add your own:

1. Edit `documents_db.py` to include your documents
2. Run `embed_and_store_documents.py` to embed and store them

## Usage

You can run commands manually or use the provided Makefile for convenience.

### Manual Usage

#### 1. Embed and Store Sample Documents

```bash
python embed_and_store_documents.py
```

This creates sample documents, embeds them, and stores in ChromaDB.

#### 2. Test Document Retrieval

```bash
python rag_query.py
```

This demonstrates querying the vector database for similar documents.

#### 3. Run Full RAG Pipeline

```bash
python rag_with_generation.py
```

This runs the complete RAG pipeline with sample queries, retrieving documents and generating answers using tinyllama.

#### 4. Run Tests

```bash
python test_rag_pipeline.py
```

This performs thorough testing of the RAG pipeline, including edge cases.

### Using Makefile

The project includes a Makefile for easy command execution:

```bash
# Set up environment
make setup

# Embed documents
make embed

# Test retrieval
make query

# Run RAG pipeline
make run

# Run tests
make test

# Clean up
make clean

# Show help
make help
```

## Project Structure

```
.
├── embed_and_store.py          # Basic embedding and storage example
├── documents_db.py             # Sample documents database
├── embed_and_store_documents.py # Embed and store documents
├── rag_query.py                # Document retrieval demo
├── rag_with_generation.py      # Full RAG pipeline with generation
├── test_rag_pipeline.py        # Comprehensive testing suite
├── requirements.txt            # Python dependencies
├── setup_env.sh                # Environment setup script
├── TODO.md                     # Task tracking
├── .gitignore                  # Git ignore rules
└── chroma_db/                  # Local vector database (auto-created)
```

## Configuration

### Changing the Embedding Model

To use a different Sentence Transformer model, edit the model name in:
- `embed_and_store.py`
- `embed_and_store_documents.py`
- `rag_query.py`
- `rag_with_generation.py`

Example:
```python
model = SentenceTransformer('all-mpnet-base-v2')  # Different model
```

### Changing the Generation Model

To use a different Ollama model, edit `rag_with_generation.py`:

```python
response = ollama.generate(
    model='your-model-name',  # Change this
    prompt=prompt,
    options={
        'temperature': 0.1,
        'num_predict': 200
    }
)
```

### Database Path

The vector database is stored in `./chroma_db/`. To change this, modify the path in the scripts:

```python
client = chromadb.PersistentClient(path="./your-custom-path")
```

## Troubleshooting

### Common Issues

1. **Ollama not running**: Make sure Ollama is installed and `ollama serve` is running.

2. **Model not found**: Ensure you've pulled the model with `ollama pull tinyllama`.

3. **Import errors**: Make sure you're in the virtual environment (`source venv/bin/activate`).

4. **No documents found**: Run `embed_and_store_documents.py` first to populate the database.

5. **ChromaDB errors**: Delete the `chroma_db/` folder and re-run the embedding scripts.

### Performance Tips

- For better embeddings, use larger models like `all-mpnet-base-v2` (requires more RAM)
- Adjust `n_results` in retrieval for more/less context
- Tune Ollama parameters (temperature, num_predict) for different response styles

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open-source. Feel free to use and modify as needed.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Open an issue in the repository

---

Built with:
- Sentence Transformers for embeddings
- ChromaDB for vector storage
- Ollama for local text generation
