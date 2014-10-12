import app
from app.database import telemetry #We need the table definition
import sqlalchemy
import multiprocessing

sourcedb = sqlalchemy.create_engine(app.app.config["SOURCEDB"], echo=False);
telemetrydb = sqlalchemy.create_engine(app.app.config["TELEMETRYDB"], echo=False);
telemetrymaxid = 0

#When debug is True, instead of trying to syncronize the databases as fast as possible it increments them in steps equal to debuglimit, this can be usefull for testing how quickly the interface updates
debug = False
debuglimit = 100

#app.database.metadata.create_all(sourcedb) #Should not be needed because the database already exists, but it should produce an error if the definition doesn't match


l = multiprocessing.Lock()


def daemon():
    #What sync method are we using?
    sync, engine = sync_select()
    print sync
    #Code for running first sync
    print "Starting First Sync, if there is alot of data this could take a while"
    sync(engine)
    print "First Sync Complete, Launching Daemon"
    #Code for launching further syncs in a separate proccess here
    daemon_process = multiprocessing.Process(target=loop, name="syncloop")
    daemon_process.daemon = True
    daemon_process.start()


def loop(once=False):
    sync, engine = sync_select()
    while(1):
	try: #The Show Must go on!
	    sync(engine)
	except sqlalchemy.exc.DBAPIError:
	    pass #Raised when execution of database operations fails
	except sqlalchemy.exc.SQLAlchemyError:
	    pass #General SQLAlchemy error class


def sync_select():
	if telemetrydb.driver == "mysqldb" and sourcedb.driver == "mysqldb":
		return sync_mysql, telemetrydb
		# sync_mysql operates under the assumption that the databases are both mysql. It uses a literal sql expression to add the data that is very fast
	else:
		return sync_sqlalchemy, app.database.engine
		# sync_sqlalchemy will take advantage of sqlalchemy's abstractions to work on most compatable databases

def sync_mysql(engine):
	telemetrymaxid = maxid(engine)
	#Query for values greater than the ones that we have
	if debug:
		s = sqlalchemy.sql.expression.text("INSERT INTO telemetry.telemetry SELECT * FROM telemetry WHERE telemetry.id > :telemetrymaxid ORDER BY telemetry.id LIMIT :limit").bindparams(telemetrymaxid=telemetrymaxid, limit=debuglimit)
	else:
		s = sqlalchemy.sql.expression.text("INSERT INTO telemetry.telemetry SELECT * FROM telemetry WHERE telemetry.id > :telemetrymaxid ORDER BY telemetry.id").bindparams(telemetrymaxid=telemetrymaxid)
	sourcedb.execute(s)


def sync_sqlalchemy(engine):
	l.acquire()
	telemetrymaxid = maxid(engine)
	l.release()
	if debug:
		s = sqlalchemy.sql.select([telemetry]).where(telemetry.c.id > telemetrymaxid).limit(debuglimit)
	else:
		s = sqlalchemy.sql.select([telemetry]).where(telemetry.c.id > telemetrymaxid)
	result = sourcedb.execute(s).fetchall()
	#Error will be produced here if result contains to data, but it will get handled in the try except in loop()
	s = sqlalchemy.sql.insert(telemetry)
	l.acquire()
	engine.execute(s, result)
	l.release()
	


def maxid(engine):
	s = sqlalchemy.sql.select([sqlalchemy.func.max(telemetry.c.id)])
	result = engine.execute(s).fetchall()[0][0]
	if result is None:
		result = 0
	return result
