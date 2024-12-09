#Given:

    #A secretary wishes to book a number of places for a competition

#When:

    #They book a number of places on a competition that has happened in the past

#Then:

    #They receive a confirmation message

#Expected:

    #They should not be able to book a place on a post-dated competition 
    #(but past competitions should be visible). 

#The booking.html page should be displayed for a valid competition.

#An error message is displayed when a competition is invalid 
    #and a confirmation message is displayed when a competition is valid
    
import pytest
from datetime import datetime, timedelta
from server import validate_competition_date


def test_competition_date_valid():
    future_date = datetime.now() + timedelta(days=1)
    competition_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    assert validate_competition_date(competition_date) is True

def test_competition_date_past():
    future_date = datetime.now() - timedelta(days=1)
    competition_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    with pytest.raises(ValueError, match="The competition date has passed."):
        validate_competition_date(competition_date)
