import pytest
from server import app

@pytest.fixture
def client():
    """Fixture for Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
