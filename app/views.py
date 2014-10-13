from app import app
from app.variables import variables
import flask
import app.database as database
import simplejson #pip install simplejson #simplejson has beter decimal support than the standard json library

def template(name, **kwargs):
	return flask.render_template(name, variables=variables, displayvars=sorted(variables.keys()), **kwargs)

	
def encode(values):
	return flask.Response(simplejson.dumps(values, use_decimal=True, #If use_decimal is not used the encoder will use "strings"
						  sort_keys = True, indent = 4, ensure_ascii=False), mimetype='application/json') #Makes the json returned easily readable
'''
Data
'''
@app.route("/<data>/current")
def current_data(data):
	value = database.selectcurrent(#Only want one value (LIMIT 1)
								selection=[variables[data].data] #SELECT data from the columns specified
								)[0] #Function returns an Array with one value so we have to enter it
	return encode(value)

	
@app.route("/<data>/number")
def number(data):
	return template("number.html", title="Number Display of {data}".format(data=variables[data].display), var=data)

	
@app.route("/<data>/number/data")
def number_data(data):
	value = database.selectcurrent(selection=[variables[data].data])[0]
	return encode(value)
	
	
@app.route("/<data>/short")
def short(data):
	return template("short.html", title="Short Graph of {data}".format(data=variables[data].display), var=data)

	
@app.route("/<data>/short/data")
def short_data(data):
	value = database.selectlast(1800, selection=[database.telemetry.c.epochtime, variables[data].data])
	return encode(value)
	

@app.route("/<data>/gauge")
def gauge(data):
	return template("gauge.html", title="Gauge of {data}".format(data=variables[data].display), var=data)

	
@app.route("/<data>/gauge/data")
def gauge_data(data):
	value = database.selectcurrent(selection=[variables[data].data])[0]
	return encode(value)
	

@app.route("/<data>/long")
def long(data):
	return template("long.html", title="Long Graph of {data}".format(data=variables[data].display), var=data)
	

@app.route("/<data>/long/data/")
@app.route("/<data>/long/data/<int:start>/<int:end>/")
def long_data(data, start=0, end=None):
	values = database.selectdist(200, selection=[database.telemetry.c.epochtime, variables[data].data], min=start, max=end)
	return encode(values)


'''
End of Data Section
'''


@app.route('/')
@app.route('/index')
@app.route('/dash')
def dash():
	return template("base.html", title="Dash")


@app.route('/dash/data')
def dash_data():
	return


@app.route('/raw')
def raw():
	return template("raw.html", title="Raw")


@app.route('/map')
def map():
	return


@app.route("/all/current")
def all_current():
	result = database.selectcurrent(selection=[variables[attr].data for attr in sorted(variables.keys())])[0]
	keys = sorted(variables.keys())
	values = dict(zip(keys, result))
	return encode(values)


@app.route("/export.csv")
def export():
    data = database.selectall()
    values = [str(col) for col in database.telemetry.c]
    render = flask.render_template("export.csv", database=data, values=values)
    return flask.Response(render, mimetype='text/csv')
