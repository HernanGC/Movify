from ..resourceModels.Genres import Genres
from ..helpers.Data import DataHelper

Genres = Genres()
data_helper = DataHelper()


class Genres:

    def get_genres():
	    genres = sess.query(Genres).first()
	    return data_helper.row_to_dict(genres)