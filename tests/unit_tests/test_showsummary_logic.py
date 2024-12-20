import pytest

from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_showSummary_unknown_email(client, mocker):
    """Test showSummary route with an invalid email."""
    mocker.patch('server.clubs', [
        {"name": "Test Club", "email": "valid@club.com", "points": "10"}
    ])
    response = client.post('/showSummary', data={'email': 'invalid@club.com'})
    error_message = b"Sorry, that email wasn&#39;t found."
    assert response.status_code == 404
    assert error_message in response.data

def test_showSummary_known_email(client, mocker):
    """Test showSummary route with a valid email."""
    mocker.patch('server.clubs', [
        {"name": "Test Club", "email": "valid@club.com", "points": "10"}
    ])
    response = client.post('/showSummary', data={'email': 'valid@club.com'})
    assert response.status_code == 200