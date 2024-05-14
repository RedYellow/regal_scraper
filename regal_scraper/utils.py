from dateutil import relativedelta
from datetime import datetime

def get_last_friday():
	return (datetime.now() + relativedelta.relativedelta(weekday = relativedelta.FR(-1))).date()