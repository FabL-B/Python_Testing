import pytest

from server import validate_max_places, MAX_PLACES_PER_COMPETITION


def test_valid_max_places():
    places_required = 10
    assert validate_max_places(places_required) is True

def test_excessive_max_places():
    places_required = 20
    error_message = (
        f"Cannot book more than {MAX_PLACES_PER_COMPETITION} places."
    )
    with pytest.raises(ValueError, match=error_message):
        validate_max_places(places_required)
