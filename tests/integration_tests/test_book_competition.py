import pytest
from datetime import datetime, timedelta

from server import app


@pytest.fixture
def mock_data(monkeypatch):
    """Mock global variables clubs and competitions."""
    test_club = [
        {"name": "Test Club",
         "email": "test@club.com",
         "points": "30"}
    ]
    test_competitions = [
        {
            "name": "Future Competition",
            "date": (
                datetime.now() + timedelta(days=10)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "numberOfPlaces": "20"
        },
        {
            "name": "Past Competition",
            "date": (
                datetime.now() - timedelta(days=10)
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "numberOfPlaces": "20"
        }
    ]

    monkeypatch.setattr('server.clubs', test_club)
    monkeypatch.setattr('server.competitions', test_competitions)
    
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_book_with_mocked_data(mock_data, client):
    response = client.get('/book/Future Competition/Test Club')
    assert response.status_code == 200
    assert b"Booking for Future Competition" in response.data

def test_expired_comptetion_cannot_be_booked(mock_data, client):
    response = client.get('/book/Past Competition/Test Club')
    assert response.status_code == 200
    assert b"The competition date has passed." in response.data
