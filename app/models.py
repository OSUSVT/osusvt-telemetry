from app import app
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property

engine = create_engine(app.config["CONNECT"])
Base = declarative_base(engine)

class Telemetry(Base):
    __tablename__ = 'telemetry'
    __table_args__ = {'autoload':True}
    Index = Column(Integer, primary_key=True)
    """This is How You Can Define Calculated Fields that are not in the Database"""
    @hybrid_property
    def Efficiency(self):
	return float(self.__getattribute__("ArrayCurrent")) - float(self.__getattribute__("MainPackCurrent"))

def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

