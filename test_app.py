import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_query_with_relevant_documents(client):
    # This query should return relevant documents and an answer
    response = client.post('/query', data={'query': 'What is retrieval-augmented generation?'})
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'answer' in json_data
    assert json_data['answer'] != 'No relevant documents found for your query.'

def test_query_with_no_relevant_documents(client):
    # This query should return no relevant documents message
    response = client.post('/query', data={'query': 'asdkfjhasdkfjhasdfkjhasdf'})
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data.get('answer') == 'No relevant documents found for your query.'

def test_query_with_empty_query(client):
    # This should return an error for no query provided
    response = client.post('/query', data={'query': ''})
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data

def test_query_with_missing_query(client):
    # This should return an error for missing query parameter
    response = client.post('/query', data={})
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data
