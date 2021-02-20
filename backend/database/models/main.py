from .Search import Search
from ..base import Session
from pprint import pprint


def get_search():
    session = Session()
    # search = Search()
    search_obj = session.query(Search).first() 
    pprint(search_obj)
    return row_to_dict(search_obj)


def row_to_dict(row):
    dic = {}
    for column in row.__table__.columns:
        dic[column.name] = str(getattr(row, column.name))
    return dic