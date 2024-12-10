import pytest

from server import update_club_points

#Given:

    #A club secretary wishes to redeem points for a place in a competition

#When:

    #The number of places is confirmed

#Then:

    #The amount of club points available remain the same

#Expected:

    # The amount of points used should be deducted from the club's balance.

def test_valid_club_points_update():
    club = {'name': 'club test', 'points': '10'}
    places_required = 4
    print("Before update:", type(club['points']), club['points'])
    update_club_points(club=club, placesRequired=places_required)
    print("After update:", type(club['points']), club['points'])
    assert club['points'] == '6'