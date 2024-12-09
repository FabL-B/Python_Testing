import pytest

from server import app, MAX_PLACES_PER_COMPETITION


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_club_can_reserve_requested_places(client):
    """Test a valid purchase where the club has enough points."""
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Iron Temple',
        'places': 2
        })
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

def test_club_cannot_reserve_excessive_places(client):
    """Test a purchase with more points than the club has."""
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Iron Temple',
        'places': 50
        })
    error_message = b"Not enough points available."
    assert response.status_code == 400
    assert error_message in response.data

def test_club_cannot_reserve_above_max_places(client):
    """Test a purchase with more points than the club has."""
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': 13
        })
    max_places = MAX_PLACES_PER_COMPETITION
    error_message = f"Cannot book more than {max_places} places."
    error_message = error_message.encode()
    assert response.status_code == 400
    assert error_message in response.data
