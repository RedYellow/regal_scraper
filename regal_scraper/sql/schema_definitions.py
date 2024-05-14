theatres_schema ="""CREATE TABLE IF NOT EXISTS theatres (
	name TEXT,
	path_name TEXT,
	theatre_code TEXT PRIMARY KEY,
	message_start TEXT,
	message_end TEXT,
	message_title TEXT,
	theatre_info_message TEXT,
	address TEXT,
	city TEXT,
	state TEXT,
	postal_code TEXT,
	latitude REAL,
	longitude REAL,
	phone_number TEXT,
	pwp_availability INTEGER,
	iana_timezone TEXT,
	value_day_text TEXT,
	unlimited_tier INTEGER
    );
    """