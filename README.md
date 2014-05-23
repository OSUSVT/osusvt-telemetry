OSUSVT-Telemetry
================

Currently (May 2014) my playground for this project

###Development Setup
1. Get the repo
```
git clone ...
cd osusvt-telemetry
```
2. Insure that VirtualEnv and the Python Development Headers are Installed
```
# If using yum...
sudo yum install virtualenv python pip python-dev
# If using a debian
sudo apt-get install python-virtualenv python-dev
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
6. Run the development webserver
```
python devrun.py
```
PRO-TIP: Install Screen and run it in a screen it will automatically reload when you make changes


