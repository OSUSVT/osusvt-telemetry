from app import app, session, Telemetry
from flask import render_template, Response
import json, time, operator
from datetime import datetime


@app.route('/')
@app.route('/index')
@app.route('/dash')
@app.route('/dash/')
def dash():
    items = app.config["DASH"]
    return render_template("dash.html",
                           title="Dashboard",
			   items=items,
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"],
                           update=app.config["UPDATE"]*4
                           )


@app.route('/dash/data/')
def dash_data():
	num = 1200
	query = session.query(Telemetry).order_by(Telemetry.Index).limit(num)
	items = app.config["DASH"]
	values = dict()
	for item in items:
		values["current-" + item.lower()] = [round(float(query[0].__getattribute__(item)), 2)]
		values["graph-" + item.lower()] = [] #We will fill it latter
	for value in query:
		epoctime = int(time.mktime(datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').timetuple()) + 1e-6 * datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000
		for item in items:
			itemvalue = value.__getattribute__(item)
			if not itemvalue is None:
				itemvalue = float(itemvalue)
			values["graph-" + item.lower()].append((epoctime, itemvalue))
	return Response(json.dumps(values), mimetype='application/json')



@app.route('/raw')
def raw():
    return render_template("raw.html",
                           title="Raw",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"],
                           update=app.config["UPDATE"]
                           )


@app.route('/map')
def map():
    return render_template("index.html",
                           title="Map",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )


@app.route("/all/current/")
def current():
    query = session.query(Telemetry).order_by(Telemetry.Index.desc()).first()
    value = dict(query.__dict__)
    del value['_sa_instance_state']
    return Response(json.dumps(value), mimetype='application/json')


@app.route("/<data>/current")
@app.route("/<data>/current/")
def current_data(data):
    query = session.query(Telemetry).order_by(Telemetry.Index.desc()).first()
    value = [float(query.__getattribute__(data))]
    return Response(json.dumps(value), mimetype='application/json')


@app.route("/<data>/all")
@app.route("/<data>/all/")
def all_data(data):
    query = session.query(Telemetry).order_by(Telemetry.Index).all()
    values = []
    for value in query:
        #This Long Incantation Converts our string of data into Unix Time time 1000
        epoctime = int(time.mktime(datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').timetuple()) + 1e-6 * datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000
        datavalue = value.__getattribute__(data)
        if not datavalue is None:
            datavalue = float(datavalue)
        values.append((epoctime, datavalue))
    return Response(json.dumps(values), mimetype='application/json')


@app.route('/<data>/prev/<num>')
@app.route('/<data>/prev/<num>/')
def prev_data(data, num):
    query = session.query(Telemetry).order_by(Telemetry.Index).limit(num)
    values = []
    for value in query:
        #This Long Incantation Converts our string of data into Unix Time time 1000
        epoctime = int(time.mktime(datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').timetuple()) + 1e-6 * datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000
        datavalue = value.__getattribute__(data)
        if not datavalue is None:
            datavalue = float(datavalue)
        values.append((epoctime, datavalue))
    return Response(json.dumps(values), mimetype='application/json')


@app.route('/<data>/gauge')
@app.route('/<data>/gauge/')
def gauge(data):
    return render_template("gauge.html",
                           attributes=app.config["ITEMPROP"],
                           title="Gauge - {0}".format(app.config["ITEMPROP"][data]["title"]),
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"],
                           minval=app.config["ITEMPROP"][data]["minval"],
                           maxval=app.config["ITEMPROP"][data]["maxval"],
                           charttitle=app.config["ITEMPROP"][data]["title"],
                           suffix=app.config["ITEMPROP"][data]["units"],
                           data=data,
                           update=app.config["UPDATE"]
                           )


@app.route("/<data>/long")
@app.route("/<data>/long/")
def long(data):
    return render_template("long.html",
                           attributes=app.config["ITEMPROP"],
                           title="Long Chart",
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"],
                           charttitle=app.config["ITEMPROP"][data]["title"],
                           data=data
                           )


@app.route("/<data>/short")
@app.route("/<data>/short/")
def short(data):
    return render_template("short.html",
                           attributes=app.config["ITEMPROP"],
                           title="Long Chart",
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"],
                           charttitle=app.config["ITEMPROP"][data]["title"],
                           data=data,
                           suffix=app.config["ITEMPROP"][data]["units"],
                           update=app.config["UPDATE"]
                           )


@app.route('/mysql/soft')
def mysql_soft():
    return render_template("index.html",
                           title="MySQL Soft Reset",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )


@app.route('/mysql/hard')
def mysql_hard():
    return render_template("index.html",
                           title="MySQL Hard Reset",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )

