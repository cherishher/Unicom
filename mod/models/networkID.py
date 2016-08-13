# -*- coding: utf-8 -*-
# @Date    : 2016/8/11  19:09
# @Author  : 490949611@qq.com

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class networkID(Base):
	__tablename__ = 'networkID'
	key = Column(Integer,primary_key=True)
	useid = Column(String(64),nullable=False)
	wiredid = Column(String(64),nullable=False)
	wirelessid = Column(String(64),nullable=False)
	time = Column(Integer,nullable=2)

if __name__ == '__main__':
	Base.metadata.create_all(engine)