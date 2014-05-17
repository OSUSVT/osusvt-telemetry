import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLUSERNAME = 'osusvtremote'
SQLPASSWORD = 'Phenix'
SQLDATABASE = 'Telemetry'


#SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://" + SQLUSERNAME + ":" + SQLPASSWORD + "@localhost/" + SQLDATABASE + "?charset=utf8&use_unicode=0"
SQLALCHEMY_DATABASE_URI = "sqlite:////"+basedir+"app.db"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
