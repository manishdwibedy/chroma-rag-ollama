from flask import Flask, request, jsonify, render_template
from rag_with_generation import rag_pipeline, generate_answer, retrieve_documents

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form.get('query')

    print(user_query)
    if not user_query:
        return jsonify({'error': 'No query provided'}), 400

    # Retrieve documents
    results = retrieve_documents(user_query)
    retrieved_docs = [metadata for metadata in results['metadatas'][0]]
    distances = results['distances'][0]

    # Check if any relevant documents were found with sufficient similarity
    if not retrieved_docs or max((1 - d / 2) for d in distances) < 0.3:
        return jsonify({'answer': 'No relevant documents found for your query.'})

    # Generate answer
    answer = generate_answer(user_query, retrieved_docs)

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
