import sys
from datetime import datetime

new = sys.argv[1]

print new

from app import db,models

s = models.body_control(time = datetime.now(), soc = new)
db.session.add(s)
db.session.commit()
