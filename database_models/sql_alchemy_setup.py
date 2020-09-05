from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

CONN_STRING = str(os.environ.get('JAWSDB_URL'))

engine = create_engine(CONN_STRING, echo=True)

Session = sessionmaker(bind=engine.connect())
session = Session()

Base = declarative_base()