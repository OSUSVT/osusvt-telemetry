import app
from app.database import telemetry #We need the table definition
import sqlalchemy
import time

sourcedb = sqlalchemy.create_engine(app.app.config["SOURCEDB"], echo=False);
telemetrydb = sqlalchemy.create_engine(app.app.config["TELEMETRYDB"], echo=False);
telemetrymaxid = 0
sourcemaxid = 0

debug = True

#app.database.metadata.create_all(sourcedb) #Should not be needed because the database already exists, but it should produce an error if the definition doesn't match



def daemon():
    #Code for running first sync
    print "Starting First Sync, if there is alot of data this could take a while"
    sync()
    print "First Sync Complete, Launching Daemon"
    #Code for launching further syncs in a separate proccess here

@app.timeit
def sync():
    telemetrymaxid = maxid(telemetrydb)
    sourcemaxid = maxid(sourcedb)
    if countrows(sourcedb) or sourcemaxid > telemetrymaxid:
	#Query for values greater than the ones that we have
	s = sqlalchemy.sql.select([telemetry]).order_by(telemetry.c.id).where(telemetry.c.id > telemetrymaxid).limit(10)
	result = sourcedb.execute(s).fetchall() #get data from source
	sourcedb.execute(s) #get data from source


def countrows(engine):
	s = sqlalchemy.sql.select([sqlalchemy.func.count(telemetry.c.id)])
	result = engine.execute(s).fetchall()[0][0]
	if result is None:
		result = 0
	return result


def maxid(engine):
	s = sqlalchemy.sql.select([sqlalchemy.func.max(telemetry.c.id)])
	result = engine.execute(s).fetchall()[0][0]
	if result is None:
		result = 0
	return result
