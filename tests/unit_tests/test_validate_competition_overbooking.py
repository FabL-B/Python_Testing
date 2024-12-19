import pytest

from server import validate_competition_overbooking


def test_valid_places():
    places_required = 10
    competition = {"name": "test competition", "numberOfPlaces": "12"}
    assert validate_competition_overbooking(competition, places_required) is True

def test_excessive_places():
    places_required = 10
    competition = {"name": "test competition", "numberOfPlaces": "5"}
    error_message = (
        f"Not enough places available in the competition."
    )
    with pytest.raises(ValueError, match=error_message):
        validate_competition_overbooking(competition, places_required)