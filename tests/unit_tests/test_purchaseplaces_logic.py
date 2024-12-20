  
import pytest
from server import app, MAX_PLACES_PER_COMPETITION


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_purchase_places_success(mocker, client):
    """Test a successful purchase where points and places are deducted."""
    mock_competitions = [
        {"name": "Test Competition", "date": "2026-10-22 13:30:00", "numberOfPlaces": "10"}
    ]
    mock_clubs = [
        {"name": "Test Club", "email": "test@club.com", "points": "10"}
    ]
    mocker.patch('server.competitions', mock_competitions)
    mocker.patch('server.clubs', mock_clubs)
    mocker.patch('server.validate_competition_overbooking', return_value=True)
    mocker.patch('server.validate_club_points', return_value=True)
    mocker.patch('server.validate_max_places', return_value=True)

    response = client.post('/purchasePlaces', data={
        'competition': 'Test Competition',
        'club': 'Test Club',
        'places': 2
    })

    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    assert int(mock_competitions[0]["numberOfPlaces"]) == 8
    assert int(mock_clubs[0]["points"]) == 8


def test_purchase_places_fail_max_places_validation(mocker, client):
    """Test purchase failure with exceeding max places limit."""
    mocker.patch('server.competitions', [
        {"name": "Test Competition", "date": "2026-10-22 13:30:00", "numberOfPlaces": "30"}
    ])
    mocker.patch('server.clubs', [
        {"name": "Test Club", "email": "test@club.com", "points": "50"}
    ])
    mocker.patch('server.validate_competition_overbooking', return_value=True)
    mocker.patch('server.validate_club_points', return_value=True)
    mocker.patch('server.validate_max_places', side_effect=ValueError(
        f"Cannot book more than {MAX_PLACES_PER_COMPETITION} places."
    ))

    response = client.post('/purchasePlaces', data={
        'competition': 'Test Competition',
        'club': 'Test Club',
        'places': 15
    })
    error_message = (
        f"Cannot book more than {MAX_PLACES_PER_COMPETITION} places.".encode()
    )
    assert response.status_code == 400
    assert error_message in response.data


def test_purchase_places_fail_club_points_validation(mocker, client):
    """Test purchase failure with insufficient club points."""
    mocker.patch('server.clubs', [
        {"name": "Test Club", "email": "test@club.com", "points": "5"}
    ])
    mocker.patch('server.competitions', [
        {"name": "Test Competition", "date": "2026-10-22 13:30:00", "numberOfPlaces": "10"}
    ])
    mocker.patch('server.validate_competition_overbooking', return_value=True)
    mocker.patch('server.validate_club_points', side_effect=ValueError("Not enough points available."))
    mocker.patch('server.validate_max_places', return_value=True)

    response = client.post('/purchasePlaces', data={
        'competition': 'Test Competition',
        'club': 'Test Club',
        'places': 10
    })

    error_message = b"Not enough points available."
    assert response.status_code == 400
    assert b"Not enough points available." in response.data