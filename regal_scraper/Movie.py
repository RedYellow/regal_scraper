from dataclasses import dataclass
from datetime import datetime

@dataclass
class Showing:
	Auditorium: int
	PerformanceId: int
	PerformanceAttributes: list[str]
	PerformanceGroup: str
	CalendarShowTime: str
	UtcShowTime: str
	UnixTime: int
	StopSales : bool

	def __post_init__(self):
		self.utc_showtime = datetime.fromisoformat(self.UtcShowTime)
		self.calendar_showtime = datetime.fromisoformat(self.CalendarShowTime)


@dataclass
class Movie:
	title: str
	performances: dict
	
	def __post_init__(self):
		self.performances = [Showing(**_) for _ in self.performances]

	# utc_date: datetime
	# def __init__(movie_dict):
	# 	# dict is from the API response
	# 	title = movie_dict["Title"]
	# 	performances
	