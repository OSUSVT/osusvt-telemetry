import os

CONNECT = 'mysql+mysqldb://OSUSVT:ManBearPig@localhost/solarcar'

ORGNAME = "OSU Solar Vehicle Team"
CARNAME = "Phoenix"


UPDATE = 5000

"""
+-----------------+------------+------+-----+---------+-------+
| Field           | Type       | Null | Key | Default | Extra |
+-----------------+------------+------+-----+---------+-------+
| Index           | mediumtext | YES  |     | NULL    |       |
| DateTime        | text       | YES  |     | NULL    |       |
| Latitude        | text       | YES  |     | NULL    |       |
| Longitude       | text       | YES  |     | NULL    |       |
| Elevation       | text       | YES  |     | NULL    |       |
| Velocity        | text       | YES  |     | NULL    |       |
| MainPackSOC     | text       | YES  |     | NULL    |       |
| MainPackVoltage | text       | YES  |     | NULL    |       |
| MainPackCurrent | text       | YES  |     | NULL    |       |
| ArrayCurrent    | text       | YES  |     | NULL    |       |
| AuxPackVoltage  | text       | YES  |     | NULL    |       |
+-----------------+------------+------+-----+---------+-------+
"""
ITEMPROP = dict({
    "Efficiency": {
        "title": "Approximate Efficiency",
        "minval": -1000,
        "maxval": 1000,
        "units": "units"
    },
    "Elevation": {
        "title": "Elevation",
        "minval": 0,
        "maxval": 1000,
        "units": "units"
    },
    "Velocity": {
        "title": "Velocity",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "MainPackSOC": {
        "title": "Main Pack State of Charge",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "MainPackCurrent": {
        "title": "Main Pack Current",
        "minval": 0,
        "maxval": 100,
        "units": "units"
    },
    "MainPackVoltage": {
        "title": "Main Pack Voltage",
        "minval": 0,
        "maxval": 200,
        "units": "units"
    },
    "ArrayCurrent": {
        "title": "Array Current",
        "minval": 0,
        "maxval": 200,
        "units": "units"
    },
    "AuxPackVoltage": {
        "title": "Auxilury Pack Voltage",
        "minval": 0,
        "maxval": 2000,
        "units": "units"
    }
})
