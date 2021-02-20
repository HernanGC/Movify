import sqlalchemy
from sqlalchemy import Column, String, Integer, Date
import datetime

from ..base import Base, sess
from ..helpers.Data import DataHelper

data_helper = DataHelper()

class Search(Base):
	

	__tablename__ = 'search'

	id          = Column(Integer, primary_key=True, autoincrement=True)
	title       = Column(String)
	type        = Column(String)
	year        = Column(String)
	imdbID      = Column(String)
	poster      = Column(String)
	created_at  = Column(Date)

	def __init__(self, title, type, year, imdbID, poster):
		self.title = title
		self.type = type
		self.year = year
		self.imdbID = imdbID
		self.poster = poster



def get_search():
	search = sess.query(Search).first()
	return data_helper.row_to_dict(search)

