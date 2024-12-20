import pytest
from server import app, loadClubs, loadCompetitions

@pytest.fixture
def client():
    """Configure Flask client for integration tests."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_data(mocker):
    """Mock initial data for integration tests."""
    mock_clubs = [
        {"name": "Test Club", "email": "test@club.com", "points": "10"}
    ]
    mock_competitions = [
        {"name": "Test Competition", "date": "2026-10-22 13:30:00", "numberOfPlaces": "10"}
    ]

    mocker.patch('server.loadClubs', return_value=mock_clubs)
    mocker.patch('server.loadCompetitions', return_value=mock_competitions)
    mocker.patch('server.clubs', mock_clubs)
    mocker.patch('server.competitions', mock_competitions)

    return {
        "clubs": mock_clubs,
        "competitions": mock_competitions
    }

def test_integration_workflow(client, mock_data):
    """
    Integration test for server.py.
    Simulate user actions across routes: loadClubs, loadCompetitions,
    index, showSummary, book, purchasePlaces, logout.
    """
    # Load clubs and competitions
    clubs = mock_data["clubs"]
    competitions = mock_data["competitions"]
    assert len(clubs) == 1
    assert len(competitions) == 1

    # Access index route
    response = client.get('/')
    assert response.status_code == 200

    # Show summary with a valid email
    response = client.post('/showSummary', data={'email': 'test@club.com'})
    assert response.status_code == 200

    # Book a competition
    response = client.get('/book/Test%20Competition/Test%20Club')
    assert response.status_code == 200
    assert b"Booking for Test Competition" in response.data

    # Purchase places successfully
    response = client.post('/purchasePlaces', data={
        'competition': 'Test Competition',
        'club': 'Test Club',
        'places': 2
    })
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

    # Verify updated points and places
    assert int(competitions[0]["numberOfPlaces"]) == 8
    assert int(clubs[0]["points"]) == 8

    # Logout
    response = client.get('/logout')
    assert response.status_code == 302  # Ensure redirection to index
    assert response.headers["Location"] == "/"
