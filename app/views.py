from app import app, db, models
from flask import render_template, Response
import json, time, operator
from datetime import datetime

ORGNAME = "OSU Solar Vehicle Team"
CARNAME = "Pheonix"

gaugesettings = dict({
    "mainpacksoc": {
        "title": "State of Charge (Main Pack)",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "elevation": {
        "title": "Elevation",
        "minval": 0,
        "maxval": 1000,
        "units": "units"
    },
    "velocity": {
        "title": "Velocity",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "mainpackvoltage": {
        "title": "Main Pack Voltage",
        "minval": 0,
        "maxval": 200,
        "units": "units"
    }
})
guageupdate = 5000


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title="Welcome",
                           carname=CARNAME,
                           orgname=ORGNAME
                           )


@app.route("/<data>/current")
@app.route("/<data>/current/")
def current_data(data):
    query = models.telemetry.query.order_by(models.telemetry.identity.desc()).first()
    # This is bad codding find a different way...
    exec ("value = [query." + data + " ]")
    return Response(json.dumps(value), mimetype='application/json')


@app.route("/<data>/all")
@app.route("/<data>/all/")
def all_data(data):
    query = models.telemetry.query.order_by(models.telemetry.identity.desc()).all()
    values = []
    exec ("values = [(int(time.mktime(datetime.strptime(value.datetime, '%m/%d/%Y %H:%M:%S %p').timetuple())+1e-6*datetime.strptime(value.datetime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000, value." + data + ") for value in query]")
    #values.sort(reverse=True)
    values.reverse()
    return Response(json.dumps(values), mimetype='application/json')


@app.route('/<data>/prev/<num>')
@app.route('/<data>/prev/<num>/')
def prev_data(data, num):
    query = models.telemetry.query.order_by(models.telemetry.identity.desc()).limit(num)
    values = []
    exec ("values = [(int(time.mktime(datetime.strptime(value.datetime, '%m/%d/%Y %H:%M:%S %p').timetuple())+1e-6*datetime.strptime(value.datetime, '%m/%d/%Y %H:%M:%S %p').microsecond) * 1000, value." + data + ") for value in query]")
    #values.sort(reverse=True)
    values.reverse()
    return Response(json.dumps(values), mimetype='application/json')


@app.route('/<data>/gauge')
@app.route('/<data>/gauge/')
def gauge(data):
    return render_template("gauge.html",
                           title="Gauge - {0}".format(gaugesettings[data]["title"]),
                           carname=CARNAME,
                           orgname=ORGNAME,
                           minval=gaugesettings[data]["minval"],
                           maxval=gaugesettings[data]["maxval"],
                           charttitle=gaugesettings[data]["title"],
                           suffix=gaugesettings[data]["units"],
                           data=data,
                           update=guageupdate
                           )


@app.route("/<data>/long")
@app.route("/<data>/long/")
def chart(data):
    return render_template("long.html",
                           title="Long Chart",
                           carname=CARNAME,
                           orgname=ORGNAME,
                           data=data,
                           )