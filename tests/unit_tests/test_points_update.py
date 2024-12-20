import pytest

from server import update_club_points


def test_valid_club_points_update():
    club = {'name': 'club test', 'points': '10'}
    placesRequired = 4
    print("Before update:", type(club['points']), club['points'])
    update_club_points(club=club, places_required=placesRequired)
    print("After update:", type(club['points']), club['points'])
    assert club['points'] == '6'
