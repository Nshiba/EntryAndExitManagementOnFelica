#-*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import sys

DATABASE = ''

#setup sqlalchemy
engine = create_engine(DATABASE, encoding='utf-8')
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Zanryu_log(Base):
  __tablename__ = 'zanryu_log';
  _id = Column('_id', BigInteger, primary_key=True)
