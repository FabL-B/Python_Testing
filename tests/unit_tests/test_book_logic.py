import pytest
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_book_route_valid(client, mocker):
    """Test book route with valid club and competition."""
    mocker.patch('server.competitions', [
        {"name": "Test Competition",
         "date": "2026-10-22 13:30:00",
         "numberOfPlaces": "10"
         }
    ])
    mocker.patch('server.clubs', [
        {"name": "Test Club", "email": "test@club.com", "points": "10"}
    ])
    mocker.patch('server.validate_competition_date', return_value=True)
    response = client.get('/book/Test%20Competition/Test%20Club')
    assert response.status_code == 200
    assert b"Booking for Test Competition" in response.data


def test_book_route_invalid_competition(client, mocker):
    """Test book route with a competition that has passed."""
    mocker.patch('server.competitions', [
        {"name": "Test Competition",
         "date": "2026-10-22 13:30:00",
         "numberOfPlaces": "10"
         }
    ])
    mocker.patch('server.clubs', [
        {"name": "Test Club", "email": "test@club.com", "points": "10"}
    ])
    mocker.patch(
        'server.validate_competition_date',
        side_effect=ValueError("The competition date has passed.")
    )
    response = client.get('/book/Test%20Competition/Test%20Club')
    assert response.status_code == 200
    assert b"The competition date has passed." in response.data
