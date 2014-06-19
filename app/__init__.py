from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.debug = True

from models import loadSession, Telemetry
 
session = loadSession()

from app import views
