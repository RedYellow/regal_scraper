from dataclasses import dataclass
from datetime import datetime

@dataclass
class Movie:
	title: str
	utc_date: datetime
	