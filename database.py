'''
Filename: /Users/Nic/Documents/Python Projects/regal_scraper-1/database.py
Path: /Users/Nic/Documents/Python Projects/regal_scraper-1
Created Date: Wednesday, April 10th 2024, 12:36:35 pm
Author: Ryan2

Copyright (c) 2024 Your Company
'''
from pathlib import Path
import pandas as pd
import sqlite3
from sql.schema_definitions import theatres_schema
class DataBase():
	def __init__(self):
		self._load_theatre_data(Path("localTheatreData.csv"))

	@classmethod
	def db_conn():
		return sqlite3.connect("regal.db")


	def _load_theatre_data(self, theatre_data_path):
		df = pd.read_csv(theatre_data_path)
		df.to_sql("theatres", self.db_conn)




if __name__ == "__main__":
	print("zoop")

