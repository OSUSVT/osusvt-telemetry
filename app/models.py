#from app import app
import sqlalchemy #pip install sqlalchemy mysql-python
import sqlalchemy.types as types
import simplejson #pip install simplejson #simplejson has beter decimal support than the standard json library

engine = sqlalchemy.create_engine("mysql://OSUSVT:ManBearPig@localhost/solarcar", echo=False);
metadata = sqlalchemy.MetaData()
telemetry = sqlalchemy.Table('telemetry', metadata,
				sqlalchemy.Column('id', types.Integer(), primary_key=True, nullable=False),
				sqlalchemy.Column('epochtime', types.BigInteger()),
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
s = sqlalchemy.sql.select([telemetry]).order_by(telemetry.c.id.desc()).limit(1800)
database = list()
result = engine.execute(s)
for row in result:
	entry = tuple(row)
	database.append(entry)
with open('output.json', 'w') as outfile:
	simplejson.dump(database, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

''' #This is the code used to add the epochtime
s = sqlalchemy.sql.select([telemetry.c.id, telemetry.c.time]) #.order_by(telemetry.c.id.desc()).limit(1800)
result=engine.execute(s)
ids = []
for row in result:
	ids.append([row[0], row[1], None])
for i, row in enumerate(ids):
	epoctime = int(time.mktime(datetime.strptime(row[1], '%m/%d/%Y %H:%M').timetuple()) + 1e-6 * datetime.strptime(row[1], '%m/%d/%Y %H:%M').microsecond) * 1000
	row[2] = epoctime
	s = telemetry.update().where(telemetry.c.id == row[0]).values(epochtime=row[2])
	engine.execute(s)
	print row
'''
