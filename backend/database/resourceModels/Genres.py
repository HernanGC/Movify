import sqlalchemy
from sqlalchemy import Column, String, Integer, Date

from ..base import Base
from ..helpers.Data import DataHelper

data_helper = DataHelper()

class Genres(Base):
	

	__tablename__ = 'top_genres'

	id          = Column(Integer, primary_key=True, autoincrement=True)
	imdb_id     = Column(String)
	type        = Column(String)
	category    = Column(String)
	created_at  = Column(Date)

	def __init__(self, title, imdb_id, type, category):
		self.title = title
		self.imdb_id = imdb_id
		self.type = type
		self.category = category


    def get_genres():
	    search = sess.query(Search).first()
	    return data_helper.row_to_dict(search)
