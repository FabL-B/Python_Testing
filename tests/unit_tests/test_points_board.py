import pytest

from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_clubs(monkeypatch):
    """Mock the global clubs data."""
    test_clubs = [
        {"name": "Club A", "points": "50"},
        {"name": "Club B", "points": "30"},
        {"name": "Club C", "points": "20"}
    ]
    monkeypatch.setattr('server.clubs', test_clubs)

def test_club_points_route_accessible(client, mock_clubs):
    """Test that the club points route is accessible."""
    response = client.get('/pointsBoard')
    assert response.status_code == 200

def test_club_points_display_correct_data(client, mock_clubs):
    """Test that the club points page displays the correct data."""
    response = client.get('/pointsBoard')
    assert b"Club A" in response.data
    assert b"50" in response.data
    assert b"Club B" in response.data
    assert b"30" in response.data
    assert b"Club C" in response.data
    assert b"20" in response.data
