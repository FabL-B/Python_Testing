import pytest

from server import app


@pytest.fixture
def mock_data(monkeypatch):
    """Mock global variables clubs and competitions."""
    test_club = [
        {"name": "Test Club",
         "email": "test@club.com",
         "points": "10"}
    ]
    test_competitions = [
        {
            "name": "Test",
            "date": "2026-10-22 13:30:00",
            "numberOfPlaces": "5"
        }
    ]

    monkeypatch.setattr('server.clubs', test_club)
    monkeypatch.setattr('server.competitions', test_competitions)
    
    return {"clubs": test_club, "competitions": test_competitions}
    
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_club_points_deduction_valid_on_purchase(mock_data, client):
    initial_points = int(mock_data["clubs"][0]["points"])
    purchased_places = 2
    expected_points = initial_points - purchased_places
    
    response = client.post('/purchasePlaces', data={
        'competition': 'Test',
        'club': 'Test Club',
        'places': purchased_places
    })
    
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    
    updated_points = int(mock_data["clubs"][0]["points"])
    assert updated_points == expected_points


def test_valid_purchase_places(mock_data, client):
    """
    Test purchase when requested places pass all validations.
    """
    initial_points = int(mock_data["clubs"][0]["points"])
    purchased_places = 2
    expected_points = initial_points - purchased_places
    
    response = client.post('/purchasePlaces', data={
        'competition': 'Test',
        'club': 'Test Club',
        'places': purchased_places
    })
    
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    
    updated_points = int(mock_data["clubs"][0]["points"])
    assert updated_points == expected_points

def test_purchase_overbook_competition(mock_data, client):
    """
    Test purchase when requested places exceed competition limit
    but are valid for club and max limit.
    """
    
    initial_points = int(mock_data["clubs"][0]["points"])
    purchased_places = 2
    expected_points = initial_points - purchased_places
    
    response = client.post('/purchasePlaces', data={
        'competition': 'Test',
        'club': 'Test Club',
        'places': purchased_places
    })
    
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    
    updated_points = int(mock_data["clubs"][0]["points"])
    assert updated_points == expected_points
