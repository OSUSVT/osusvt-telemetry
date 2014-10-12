import app
import sqlalchemy #pip install sqlalchemy mysql-python
import sqlalchemy.types as types


engine = sqlalchemy.create_engine(app.app.config["TELEMETRYDB"], echo=False);
metadata = sqlalchemy.MetaData()
telemetry = sqlalchemy.Table('telemetry', metadata,
				sqlalchemy.Column('id', types.Integer(), primary_key=True, nullable=False),
				sqlalchemy.Column('epochtime', types.BigInteger(), nullable=False),
				sqlalchemy.Column('time', types.CHAR(length=16), nullable=False),
				sqlalchemy.Column('latitude', types.Numeric(precision=12, scale=6), nullable=False),
				sqlalchemy.Column('longitude', types.Numeric(precision=12, scale=6), nullable=False),
				sqlalchemy.Column('elevation', types.Numeric(precision=10, scale=4), nullable=False),
				sqlalchemy.Column('velocity', types.Numeric(precision=10, scale=4), nullable=False),
				sqlalchemy.Column('mainpacksoc', types.Numeric(precision=10, scale=4), nullable=False),
				sqlalchemy.Column('mainpackcurrent', types.Numeric(precision=10, scale=4), nullable=False),
				sqlalchemy.Column('voltagemainpackcurrent', types.Numeric(precision=10, scale=4), nullable=False),
				sqlalchemy.Column('arraycurrent', types.Numeric(precision=10, scale=4), nullable=False),
				sqlalchemy.Column('auxpackvoltage', types.Numeric(precision=10, scale=4), nullable=False)
			)
metadata.create_all(engine) #Create Database if it doesn't exist


def storeresult(result):
	#This defines the format that all the arrays are returned with
	database = list()
	for row in result:
		entry = tuple(row)
		database.append(entry)
	return database


def selectall(selection=[telemetry]):
	s = sqlalchemy.sql.select(selection).order_by(telemetry.c.id.desc())
	return storeresult(engine.execute(s))
	
	
def selectlast(num, selection=[telemetry]):
	s = sqlalchemy.sql.select(selection).order_by(telemetry.c.id.desc()).limit(num)
	return storeresult(engine.execute(s))


def selectevery(num, min=1, max=None, selection=[telemetry]):
	"""Min and max refer to epoch time. If Min is specified max should be also"""
	if max:
		s = sqlalchemy.sql.select(selection).order_by(telemetry.c.epochtime).where(telemetry.c.epochtime >= min).where((telemetry.c.id - 1) % num == 0).where(telemetry.c.epochtime <= max)
	else:
		s = sqlalchemy.sql.select(selection).order_by(telemetry.c.epochtime).where((telemetry.c.id - 1) % num == 0)
	return storeresult(engine.execute(s))
	

def countrows():
	s = sqlalchemy.sql.select([sqlalchemy.func.count(telemetry.c.id)])
	result = engine.execute(s).fetchall()[0][0]
	return result

	
def minid():
	s = sqlalchemy.sql.select([sqlalchemy.func.min(telemetry.c.id)])
	result = engine.execute(s).fetchall()[0][0]
	return result
	
	
def maxid():
	s = sqlalchemy.sql.select([sqlalchemy.func.max(telemetry.c.id)])
	result = engine.execute(s).fetchall()[0][0]
	return result


def minepoch():
	s = sqlalchemy.sql.select([sqlalchemy.func.min(telemetry.c.epochtime)])
	result = engine.execute(s).fetchall()[0][0]
	return result
	
	
def maxepoch():
	s = sqlalchemy.sql.select([sqlalchemy.func.max(telemetry.c.epochtime)])
	result = engine.execute(s).fetchall()[0][0]
	return result

		
def selectdist(num, min=1, max=None, selection=[telemetry]):
	"""Min and max refer to epoch time. If Min is specified Max should be also"""
	if max:
		s = sqlalchemy.sql.select([sqlalchemy.func.count(telemetry.c.id)]).where((telemetry.c.id - 1) % num == 0).where(telemetry.c.epochtime <= max)
		countnum = engine.execute(s).fetchall()[0][0]
	else:
		countnum = countrows()
	if num > countnum:
		skipnum = 1
	else:
		skipnum = countnum/(num - 1)
	return selectevery(skipnum, min, max, selection)
