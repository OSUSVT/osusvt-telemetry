#This is the data from the car
SOURCEDB = 'mysql+mysqldb://solar:Phenix@localhost/solarcar'

#This is the Database used by Telemetry to display data, there are two basic options
#TELEMETRYDB = 'sqlite://'
	#Use database that only exists in memory. Use this if you want an easy setup
		#Pros: Don't require mysql on the laptop/box running Telemetry, starts fresh when code starts again
		#Cons: Slow to start up, no persistant data, sqlite doesn't support 'decimal' type so rounding errors will occur as the data gets converted to float
TELEMETRYDB = 'mysql+mysqldb://solar:Phenix@localhost/telemetry'
	#Use full mysql database. Use this for a more reliable setup
		#Pros: Fast, Persistant Data
		#Cons: MySQL can be hard to install

ORGNAME = "OSU Solar Vehicle Team"
CARNAME = "Phoenix"

#How long (in ms) should the JavaScript wait after recieving it's last update to request it again?
UPDATE = 250
