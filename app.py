from flask import Flask, request, jsonify, render_template
from rag_with_generation import rag_pipeline, generate_answer, retrieve_documents

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form.get('query')
    if not user_query:
        return jsonify({'error': 'No query provided'}), 400

    # Retrieve documents
    results = retrieve_documents(user_query)
    retrieved_docs = [metadata for metadata in results['metadatas'][0]]

    # Generate answer
    answer = generate_answer(user_query, retrieved_docs)

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
