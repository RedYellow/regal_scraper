'''
Filename: /Users/Nic/Documents/Python Projects/regal_scraper/database.py
Path: /Users/Nic/Documents/Python Projects/regal_scraper
Created Date: Wednesday, April 10th 2024, 12:36:35 pm
Author: Ryan2

Copyright (c) 2024 Your Company
'''
from pathlib import Path
import pandas as pd
import sqlite3
from sql.schema_definitions import theatres_schema
from sqlalchemy import text

class Database():
	def __init__(self):
		self._load_theatre_data(Path("prod_data/TheatreData.csv"))
		#TODO: can this data all be preloaded and saved as .db or something?

	def db_conn(self):
		return sqlite3.connect("regal.db")

	def _load_theatre_data(self, theatre_data_path):
		df = pd.read_csv(theatre_data_path, dtype = "string")
		conn = self.db_conn()
		conn.execute(theatres_schema)
		df.to_sql("theatres",conn, if_exists= "replace", index = False)
	
	def get_theatre_code_from_name(self, name):
		cur = self.db_conn().cursor()
		try:
			code, = cur.execute( "select theatre_code from theatres where name = :name", {"name": name}).fetchall()[0]
			return code
		except KeyError:
			raise ValueError(f"Given theatre name '{name}' does not exist")

	def get_path_name_from_name(self, name):
		cur = self.db_conn().cursor()
		code, = cur.execute( "select path_name from theatres where name = :name", {"name": name}).fetchall()[0]
		return code


# https://github.com/Kartones/flask-calendar/blob/master/flask_calendar/templates/calendar.html



if __name__ == "__main__":
	print("zoop")

