from app import db

class telemetry(db.Model):
    index = db.Column(db.Float)
    datetime = db.Column(db.String(64))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation = db.Column(db.Float)
    velocity = db.Column(db.Float)
    mainpacksoc = db.Column(db.Float)
    mainpackvoltage = db.Column(db.Float)
    mainpackcurrent = db.Column(db.Float)
    arraycurrent = db.Column(db.Float)
    identity = db.Column(db.Integer, primary_key=True)
    arraypower = db.Column(db.Float)
    batterypower = db.Column(db.Float)
    moterpower = db.Column(db.Float)
