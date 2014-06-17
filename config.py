import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLUSERNAME = 'osusvtremote'
SQLPASSWORD = 'Phenix'
SQLDATABASE = 'Telemetry'


#SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://" + SQLUSERNAME + ":" + SQLPASSWORD + "@localhost/" + SQLDATABASE + "?charset=utf8&use_unicode=0"
SQLALCHEMY_DATABASE_URI = "sqlite:////"+basedir+"/app.db"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


ORGNAME = "OSU Solar Vehicle Team"
CARNAME = "Phoenix"


UPDATE = 5000


ITEMPROP = dict({
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
    "mainpacksoc": {
        "title": "Main Pack State of Charge",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "mainpackcurrent": {
        "title": "Main Pack Current",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "mainpackvoltage": {
        "title": "Main Pack Voltage",
        "minval": 0,
        "maxval": 200,
        "units": "units"
    },
    "arraycurrent": {
        "title": "Array Current",
        "minval": 0,
        "maxval": 200,
        "units": "units"
    },
    "arraypower": {
        "title": "Array Power",
        "minval": 0,
        "maxval": 2000,
        "units": "units"
    },
    "batterypower": {
        "title": "Battery Power",
        "minval": 0,
        "maxval": 200,
        "units": "units"
    },
    "moterpower": {
        "title": "Motor Power",
        "minval": 0,
        "maxval": 2000,
        "units": "units"
    }
})
