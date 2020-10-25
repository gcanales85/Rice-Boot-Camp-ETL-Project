create table opioid_abuse ( 
	    Id SERIAL PRIMARY KEY,
		state_name varchar(100),
		state	varchar(50),
		year	varchar(10),
		month	varchar(15),
		indicator	varchar(500),
		data_value float	,
		percent_complete	float,
		percent_pending_investigation float
)