.PHONY: setup install embed query run test clean

# Set up virtual environment and install dependencies
setup:
	chmod +x setup_env.sh
	./setup_env.sh

# Install dependencies (if venv already exists)
install:
	source venv/bin/activate && pip install -r requirements.txt

# Embed and store documents
embed:
	source venv/bin/activate && python embed_and_store_documents.py

# Test document retrieval
query:
	source venv/bin/activate && python rag_query.py

# Run full RAG pipeline
run:
	source venv/bin/activate && python rag_with_generation.py

# Run tests
test:
	source venv/bin/activate && python test_rag_pipeline.py

# Clean up generated files
clean:
	rm -rf chroma_db/
	rm -rf venv/
	rm -rf __pycache__/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.pyd" -delete

# Help
help:
	@echo "Available commands:"
	@echo "  setup    - Set up virtual environment and install dependencies"
	@echo "  install  - Install dependencies (venv must exist)"
	@echo "  embed    - Embed and store documents"
	@echo "  query    - Test document retrieval"
	@echo "  run      - Run full RAG pipeline"
	@echo "  test     - Run comprehensive tests"
	@echo "  clean    - Clean up generated files"
	@echo "  help     - Show this help message"
