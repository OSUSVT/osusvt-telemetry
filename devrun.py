#!env/bin/python
from app import app
from app import sync

if __name__ == '__main__': #Windows Compatibility With MultiProcessing
	sync.daemon()

	app.run(debug=True, host='0.0.0.0', use_reloader=False)
