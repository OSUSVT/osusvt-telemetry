activate_this = '/var/www/html/telemetry/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/html/telemetry')

from app import app as application
