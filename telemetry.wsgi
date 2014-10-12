import os
import platform

#Virtualenv stores the activate_this script in different places depending on what os you are using
if platform.system() == "Windows":
	bindir = "Scripts"
else:
	bindir = "bin"

working_directory = os.path.dirname(__file__)

activate_this = os.path.join(working_directory,'env', bindir, 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, working_directory)

from app import sync
sync.daemon()

from app import app as application
