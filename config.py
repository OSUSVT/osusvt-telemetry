import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLUSERNAME = 'osusvtremote'
SQLPASSWORD = 'Phenix'
SQLDATABASE = 'Telemetry'


#SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://" + SQLUSERNAME + ":" + SQLPASSWORD + "@localhost/" + SQLDATABASE + "?charset=utf8&use_unicode=0"
SQLALCHEMY_DATABASE_URI = "sqlite:////"+os.path.abspath("app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


ORGNAME = "OSU Solar Vehicle Team"
CARNAME = "Pheonix"


UPDATE = 5000


ITEMPROP = dict({
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