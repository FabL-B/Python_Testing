import pytest
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_logout_route(client):
    """Test the logout route."""
    response = client.get('/logout')

    assert response.status_code == 302
    assert response.headers["Location"] == "/"

    follow_response = client.get(response.headers["Location"])
    assert follow_response.status_code == 200
