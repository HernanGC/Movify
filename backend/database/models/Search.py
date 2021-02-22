from ..base import sess
from ..resourceModels import Search

Search = Search()

class Search:
   
    def create_search(self, obj):
        sess.rollback()
        for attr in obj:
            search = Search(attr['Title'], attr['Type'], attr['Year'], attr['imdbID'], attr['Poster'])
            sess.add(search)
            sess.commit()
            sess.close()


    def get_search():
	search = sess.query(Search).first()
	return data_helper.row_to_dict(search)
