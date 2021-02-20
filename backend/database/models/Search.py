import sqlalchemy
from sqlalchemy import Column, String, Integer, Date

from ..base import Base, Session


class Search(Base):
	__tablename__ = 'search'

	id         = Column(Integer, primary_key=True)
	title      = Column(String)
	type       = Column(String)
	year       = Column(String)
	imdbID     = Column(String)
	poster     = Column(String)
	created_at = Column(Date)


	# def get_all(self):
	# 	session = Session()
	# 	return session.query()

