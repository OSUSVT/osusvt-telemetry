from app import db

class GPSData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lattitude = db.Column(db.String(64), index = True, unique = True)
    longitude = db.Column(db.String(64), index = True, unique = True)

    def __repr__(self): #How do we Print this class?
        return self.lattitude + "  " + self.longitude

class body_control(db.Model):
    time = db.Column(db.DateTime, primary_key = True)
    soc = db.Column(db.Float)
