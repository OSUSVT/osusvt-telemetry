import app.database

class Variable:
	def __init__(self, **kwargs):
		self.data = kwargs['data']
		"""SQLAlchemy Definition of the Column"""
		self.display = kwargs.get('display', str(self.data))
		"""Name Displayed on Interface"""
		self.min = kwargs.get('min', 0)
		"""Minimum value to expect from Variable, used for HighCharts charts and graphs"""
		self.max = kwargs.get('max', 100)
		"""Maximum value to expect from Variable, used for HighCharts charts and graphs"""
		self.units = kwargs.get('units', "")
		"""Maximum value to expect from Variable, used for HighCharts charts and graphs"""
		self.long = kwargs.get('long', False)
		"""Display Long graphs for this Variables"""
	
	def __repr__(self):
		return "<Variable: {display} from {min}{units} to {max}{units}>".format(display=self.display, min=self.min, max=self.max, units=self.units)

variables = dict()
"""Follow the Pattern to Make Variables appear in the Interface"""
variables['latitude'] = Variable(data=app.database.telemetry.c.latitude,
								 display="Latitude")
variables['longitude'] = Variable(data=app.database.telemetry.c.longitude,
								  display="Longitude")
variables['elevation'] = Variable(data=app.database.telemetry.c.elevation)
variables['velocity'] = Variable(data=app.database.telemetry.c.velocity)
variables['mainpacksoc'] = Variable(data=app.database.telemetry.c.mainpacksoc)
variables['mainpackcurrent'] = Variable(data=app.database.telemetry.c.mainpackcurrent)
variables['voltagemainpackcurrent'] = Variable(data=app.database.telemetry.c.voltagemainpackcurrent)
variables['arraycurrent'] = Variable(data=app.database.telemetry.c.arraycurrent)
variables['auxpackvoltage'] = Variable(data=app.database.telemetry.c.auxpackvoltage)