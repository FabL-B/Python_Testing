import pytest

from server import validate_max_places


def test_valid_max_places():
    places_requested = 10
    max_places = 12
    assert validate_max_places(places_requested, max_places) is True

def test_excessive_max_places():
    places_requested = 20
    max_places = 12
    with pytest.raises(ValueError, match=f"Cannot book more than {max_places} places."):
        validate_max_places(places_requested, max_places)