from app import app, db, models
from flask import render_template, Response
import json

ORGNAME = "OSU Solar Vehicle Team"
CARNAME = "Pheonix"

gaugesettings = dict( {
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
        title = "Welcome",
        carname = CARNAME,
        orgname = ORGNAME
    )

@app.route('/current/<data>/')
def current_data(data):
    query = models.telemetry.query.order_by(models.telemetry.identity.desc()).first()
#This is bad codding find a different way...
    exec("value = [query." + data + " ]")
    return Response(json.dumps(value), mimetype='application/json')

@app.route('/gauge/<data>/')
def gauge(data):
    return render_template("gauge.html",
        title = "Gauge - {0}".format(gaugesettings[data]["title"]),
        carname = CARNAME,
        orgname = ORGNAME,
        minval = gaugesettings[data]["minval"],
        maxval = gaugesettings[data]["maxval"],
        charttitle = gaugesettings[data]["title"],
        suffix = gaugesettings[data]["units"],
        data = data,
        update = guageupdate
        )
