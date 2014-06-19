from app import app, session, Telemetry
from flask import render_template, Response
import json, time, operator
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title="Welcome",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )


@app.route('/dash')
def dash():
    return render_template("index.html",
                           title="Dashboard",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )


@app.route('/raw')
def raw():
    return render_template("index.html",
                           title="Raw",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )


@app.route('/map')
def map():
    return render_template("index.html",
                           title="Map",
                           attributes=app.config["ITEMPROP"],
                           carname=app.config["CARNAME"],
                           orgname=app.config["ORGNAME"]
                           )


@app.route("/<data>/current")
@app.route("/<data>/current/")
def current_data(data):
    query = session.query(Telemetry).order_by(Telemetry.Index.desc()).first()
    # This is bad codding find a different way...
    value = [float(query.__getattribute__(data))]
    return Response(json.dumps(value), mimetype='application/json')


@app.route("/<data>/all")
@app.route("/<data>/all/")
def all_data(data):
    query = session.query(Telemetry).order_by(Telemetry.Index.desc()).all()
    values = []
    for value in query:
        values.append((int(time.mktime(
            datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').timetuple()) + 1e-6 * datetime.strptime(
            value.DateTime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000, float(value.__getattribute__(data))))
    #values.sort(reverse=True)
    values.reverse()
    return Response(json.dumps(values), mimetype='application/json')


@app.route('/<data>/prev/<num>')
@app.route('/<data>/prev/<num>/')
def prev_data(data, num):
    query = session.query(Telemetry).order_by(Telemetry.Index.desc()).limit(num)
    values = []
    for value in query:
        values.append((int(time.mktime(
            datetime.strptime(value.DateTime, '%m/%d/%Y %H:%M:%S %p').timetuple()) + 1e-6 * datetime.strptime(
            value.DateTime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000, float(value.__getattribute__(data))))
    #values.sort(reverse=True)
    values.reverse()
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

