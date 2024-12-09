import pytest

from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_showSummary_unknown_email(client):
    response = client.post('/showSummary', data={'email': 'unknown@example.com'})
    error_message = b"Sorry, that email wasn&#39;t found."
    assert response.status_code == 404
    assert error_message in response.data

def test_showSummary_known_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200