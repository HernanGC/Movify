from .Movies import Movies
from .TvShows import TvShows


class Main(Movies, TvShows):


    def __init__():


    def set_json_file_data(self, data: dict) -> None:
    with open('movies.txt', 'w') as json_file:
        json.dump(data, json_file)


    def get_json_file_data(self) -> dict:
        try:
            with open('movies.txt') as json_file:
                return json.load(json_file)
        except:
            return {}


    def set_data(self, data_dict: dict) -> bool:
        try:
            MOVIES.set_movie_genres_imdb_ids_obj(data_dict['movies_by_genre'])
            MOVIES.set_most_popular_movies(data_dict['popular_movies'])
            MOVIES.set_most_popular_shows(data_dict['popular_shows'])
            MOVIES.set_top_250_movies(data_dict['top_movies'])
            MOVIES.set_top_250_shows(data_dict['top_shows'])
            return True
        except:
            return False
