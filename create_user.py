from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    emailid = Column(String)
    number  = Column(String)
#----------------------------------------------------------------------
    def __init__(self, name, emailid, number):
        """"""
        self.name = name
        self.emailid = emailid
        self.number = number

# create tables
Base.metadata.create_all(engine)
