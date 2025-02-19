import pytest

from server import validate_competition_overbooking


def test_validate_competition_overbooking():
    competition = {"numberOfPlaces": "5"}
    places_required = 4
    assert validate_competition_overbooking(
        competition, places_required
    ) is True

    places_required = 6
    error_message = "Not enough places available in the competition."
    with pytest.raises(ValueError, match=error_message):
        validate_competition_overbooking(competition, places_required)
