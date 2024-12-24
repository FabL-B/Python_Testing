import pytest


def test_find_club_by_email():
    clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
         },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
    ]
    # Email exist
    email = "john@simplylift.co"
    found_club = [club for club in clubs if club['email'] == email][0]
    assert found_club is not None
    assert found_club["name"] == "Simply Lift"

    # Email do not exist
    email = "not@an.email"
    with pytest.raises(IndexError):
        found_club = [club for club in clubs if club['email'] == email][0]
