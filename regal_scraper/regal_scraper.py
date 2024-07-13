
from datetime import datetime
from database import Database
import requests
from urllib.parse import urljoin, urlencode

from Movie import Movie

# from Theatre import Theatre

class RegalAPI:
	def __init__(self):
		self.db = Database()
		self.local_theatre = None
		self.local_theatre_path_name = None
		self.base_url = "https://www.regmovies.com"

	def set_local_theatre(self, name):
		self.local_theatre = name #TODO: make this a Theatre object
		self.local_theatre_code =  self.db.get_theatre_code_from_name(name)
		self.local_theatre_path_name = self.db.get_theatre_path_name_from_name(name)


	def get_showings(self, date = datetime.now()):
		# url = self.build_url(self.base_url, "")
		url = f"https://www.regmovies.com/api/getShowtimes?theatres={self.local_theatre_code}&date={date.strftime('%m-%d-%Y')}&hoCode=&ignoreCache=false&moviesOnly=false"
		response = requests.get(url = url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"})
		# return response.json()['shows'][0]["Film"]
	
		return [Movie(film["Title"], film["Performances"]) for film in response.json()['shows'][0]["Film"]]
		
		
		 
	

	def build_url():
		...


if __name__ == "__main__":
	client = RegalAPI()
	client.set_local_theatre("Regal Edwards Mira Mesa")
	showings = client.get_showings(datetime.now().date())
	print("zoop")
	
	
