# -*- coding: utf-8 -*-
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
		self.graphs = kwargs.get('graphs', True)
		"""Display Graphs for this Variables"""
		self.number = kwargs.get('number', True)
		"""Display Basic Number Pages for this Variables"""
		self.gauges = kwargs.get('gauges', self.number)
		"""Display Guauges for this Variables"""
	
	def __repr__(self):
		return "<Variable: {display} from {min}{units} to {max}{units}>".format(display=self.display, min=self.min, max=self.max, units=self.units)
	
	def serializable(self):
		"""Creates a Serializable dictionary of the attributes of the object that can be serialized into json"""
		return {key : value for key, value in vars(self).iteritems() if key != 'data'}

variables = dict()
"""Follow the Pattern to Make Variables appear in the Interface"""
variables['latitude'] = Variable(data=app.database.telemetry.c.latitude/100,
								 display="Latitude",
								 graphs=False,
								 number=False,
								 units=u'°',
								 max=90,
								 min=-90
								 )
variables['longitude'] = Variable(data=-app.database.telemetry.c.longitude/100,
								  display="Longitude",
								  graphs=False,
								  number=False,
								  units=u'°',
								  max=180,
								  min=-180
								  )
variables['elevation'] = Variable(data=app.database.telemetry.c.elevation,
								  min=0,
								  max=1000,
								  display="Elevation",
								  gauges=False)
variables['velocity'] = Variable(data=app.database.telemetry.c.velocity,
								 display="Velocity",
								 max=75)
variables['mainpacksoc'] = Variable(data=app.database.telemetry.c.mainpacksoc,
									display="Main Pack SOC")
variables['mainpackcurrent'] = Variable(data=app.database.telemetry.c.mainpackcurrent,
										max=1024,
									    display="Main Pack Current")
variables['voltagemainpackcurrent'] = Variable(data=app.database.telemetry.c.voltagemainpackcurrent,
											   display="Voltage Main Pack Current",
											   max=700,
											   min=-100)
variables['arraycurrent'] = Variable(data=app.database.telemetry.c.arraycurrent,
									 min=-5,
									 max=128,
									 display="Array Current")
variables['auxpackvoltage'] = Variable(data=app.database.telemetry.c.auxpackvoltage,
									   display="Auxiliary Pack Voltage",
									   min=0,
									   max=30)