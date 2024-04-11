
from regal_scraper.database import Database

def test_get_theatre_code_from_name():
	db = Database()
	theatre_code = db.get_theatre_code_from_name("Regal Rancho Del Rey")
	assert theatre_code == "0361"
