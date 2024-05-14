from regal_scraper.utils import get_last_friday
from freezegun import freeze_time

from datetime import datetime

@freeze_time("2024-04-11")
def test_get_last_friday():
	assert get_last_friday() == datetime.date(2024, 4, 5)

