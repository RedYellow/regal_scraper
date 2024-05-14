
from database import Database
import requests
from urllib.parse import urljoin, urlencode

class RegalAPI:
	def __init__(self):
		self.db = Database()
		self.local_theatre = None
		self.local_theatre_path_name = None
		self.base_url = "https://www.regmovies.com"

	def set_local_theatre(self, name):
		self.local_theatre_path_name = self.db.get_theatre_code_from_name(name)
		self.local_theatre = name


	def get_showings(self, theatre_code):
		url = self.build_url(self.base_url, "")
		
		
		#  

	def build_url():
		...


if __name__ == "__main__":
	print("zoop")