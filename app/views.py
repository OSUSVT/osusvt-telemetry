from app import app


@app.route('/')
@app.route('/index')
@app.route('/dash')
@app.route('/dash/')
def dash():
	return


@app.route('/dash/data/')
def dash_data():
	return


@app.route('/raw')
def raw():
	return


@app.route('/map')
def map():
	return


@app.route("/all/current/")
def current():
	return


@app.route("/<data>/current")
@app.route("/<data>/current/")
def current_data(data):
	return


@app.route("/<data>/all")
@app.route("/<data>/all/")
def all_data(data):
	return


@app.route('/<data>/prev/<num>')
@app.route('/<data>/prev/<num>/')
def prev_data(data, num):
	return


@app.route('/<data>/gauge')
@app.route('/<data>/gauge/')
def gauge(data):
	return


@app.route("/<data>/long")
@app.route("/<data>/long/")
def long(data):
	return


@app.route("/<data>/short")
@app.route("/<data>/short/")
def short(data):
	return


@app.route('/mysql/soft')
def mysql_soft():
	return


@app.route('/mysql/hard')
def mysql_hard():
	return


@app.route("/export.csv")
def export():
	return
