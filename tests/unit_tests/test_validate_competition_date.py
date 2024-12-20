import pytest

from datetime import datetime, timedelta
from server import validate_competition_date


def test_validate_competition_date():
    future_date = datetime.now() + timedelta(days=1)
    past_date = datetime.now() - timedelta(days=1)
    competition_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    assert validate_competition_date(competition_date) is True
    
    competition_date = past_date.strftime("%Y-%m-%d %H:%M:%S")
    with pytest.raises(ValueError, match="The competition date has passed."):
        validate_competition_date(competition_date)
