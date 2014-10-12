OSUSVT Telemetry
================

Home of the Oregon State University Solar Car Team Telemetry App. This App is written in Python using the [Flask Framework](http://flask.pocoo.org/docs/0.10/) and [SqlAlchemy](http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html). The webpages produced utilize the [Highcharts API](http://www.highcharts.com/) to render graphs in javascript.

###Development Setup
1. Get the repo

  ```
  git clone ...
  cd osusvt-telemetry
  ```
2. Insure that VirtualEnv and the Python Development Headers are Installed

  ```
  # If using yum...
  sudo yum install python-virtualenv python python-pip python-devel gcc
  ```
3. Make a VirtualEnv named `env`

  ```
  virtualenv env
  ```
4. Install requirements

  ```
  pip install -r requirements.txt
  ```
5. Activate the virtualenv

  ```
  source env/bin/activate
  ```
6. Edit Config (if nessasary)

  ```
  vi config.py
  ```
7. Run the development webserver
  
  ```
  python devrun.py
  ```


PRO-TIP: Install Screen and run it in a screen it will automatically reload when you make changes


