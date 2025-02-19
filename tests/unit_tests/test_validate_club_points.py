import pytest

from server import validate_club_points


def test_valid_places_deduction():
    """Test if club has enough points for a purchase."""
    club = {'name': 'club test', 'points': '10'}
    places_required = 5
    assert validate_club_points(club, places_required) is True


def test_excessive_places_requested():
    """Test if club has enough points for a purchase."""
    club = {'name': 'club test', 'points': '10'}
    places_required = 15
    with pytest.raises(ValueError, match="Not enough points available"):
        validate_club_points(club, places_required)
