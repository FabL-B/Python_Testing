import pytest
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_pointsBoard_route(client, mocker):
    """Test pointsBoard route renders the clubs' points correctly."""
    mocker.patch('server.clubs', [
        {"name": "Club A", "points": "50"},
        {"name": "Club B", "points": "30"},
        {"name": "Club C", "points": "20"}
    ])
    response = client.get('/pointsBoard')
    assert response.status_code == 200
    assert b"Club A" in response.data
    assert b"50" in response.data
    assert b"Club B" in response.data
    assert b"30" in response.data
    assert b"Club C" in response.data
    assert b"20" in response.data
