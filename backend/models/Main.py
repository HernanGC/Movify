import json
from . import Movies, TvShows, Scraper


class Main(Movies.Movies, TvShows.TvShows):
    IMDB_IDS_FILE = 'imdb_ids.txt'
    MOVIES_DETAILS_FILE = 'movies_details.txt'
    SHOWS_DETAILS_FILE = 'tv_shows_details.txt'

    def __init__(self):
        self.write_to_file = {}
        self.movies_and_shows_data = {}
        super().__init__()

    def initializeF(self, top_mv: int = 15, popular_mv: int = 15, popular_tv_shows: int = 15) -> dict:
        imdb_ids_data = self.get_json_file_data(self.IMDB_IDS_FILE)
        movie_details_data = self.handle_movies_json(self.get_json_file_data(self.MOVIES_DETAILS_FILE), top_mv,
                                                     popular_mv)
        tv_shows_details_data = self.get_json_file_data(self.SHOWS_DETAILS_FILE)
        if not imdb_ids_data:
            self.init()
            imdb_ids_data = self.store_imdb_ids()
        self.set_imdb_ids(imdb_ids_data)
        if not movie_details_data:
            movie_details_data = self.load_movies(top_mv, popular_mv)
            self.set_json_file_data(movie_details_data, self.MOVIES_DETAILS_FILE)
        self.set_movie_data(movie_details_data)
        if not tv_shows_details_data:
            tv_shows_details_data = self.load_tv_shows(popular_tv_shows)
            self.set_json_file_data(tv_shows_details_data, self.SHOWS_DETAILS_FILE)
        return {
            'movie_details': movie_details_data,
            'tv_shows': tv_shows_details_data
        }

    def store_imdb_ids(self):
        self.write_to_file['top_movies'] = self.get_top_movies()
        self.write_to_file['top_shows'] = self.get_top_shows()
        self.write_to_file['popular_movies'] = self.get_most_popular_movies()
        self.write_to_file['popular_shows'] = self.get_most_popular_shows()
        self.write_to_file['movies_by_genre'] = self.get_genres_ids_from_html()
        self.set_json_file_data(self.write_to_file, self.IMDB_IDS_FILE)
        return self.get_json_file_data(self.IMDB_IDS_FILE)

    def store_movie_details(self):
        self.load_movies()

    def set_json_file_data(self, data: dict, file: str) -> None:
        with open(file, 'w') as json_file:
            json.dump(data, json_file)

    def get_json_file_data(self, file: str) -> dict:
        try:
            with open(file) as json_file:
                return json.load(json_file)
        except:
            return {}

    def handle_movies_json(self, json_file, qty1, qty2):
        return {
            'top_movies': json_file['top_movies'][:qty1],
            'popular_movies': json_file['popular_movies'][:qty2]
        }

    def set_imdb_ids(self, data_dict: dict) -> bool:
        try:
            self.set_movie_genres_imdb_ids_obj(data_dict['movies_by_genre'])
            self.set_most_popular_movies(data_dict['popular_movies'])
            self.set_most_popular_shows(data_dict['popular_shows'])
            self.set_top_250_movies(data_dict['top_movies'])
            self.set_top_250_shows(data_dict['top_shows'])
            return True
        except:
            return False
