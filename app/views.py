from app import app, db, models
from flask import render_template, Response
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
        title = "Welcome",
        carname = "Pheonix",
        orgname = "OSU Solar Vehicle Team")

@app.route('/current/<data>/')
def current_data(data):
    if(data == 'soc'):
        soc = models.body_control.query.order_by(models.body_control.time.desc()).first()
        lsoc = [soc.soc]
        return Response(json.dumps(lsoc), mimetype='application/json')

@app.route('/gauge/<data>/')
def gauge(data):
    return render_template("chart.html")
