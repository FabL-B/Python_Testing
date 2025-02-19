import pytest

from server import validate_positive_places


def test_validate_max_places():
    places_required = 10
    assert validate_positive_places(places_required) is True

    places_required = -3
    error_message = (
        f"The number of places must be a positive value."
    )
    with pytest.raises(ValueError, match=error_message):
        validate_positive_places(places_required)