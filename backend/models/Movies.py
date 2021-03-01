from .Omdb import Omdb

class Movies(Omdb):
    

    def __init__(self):
        self.movie_data: dict  = {}


    def set_movie_data(self, movie_data: dict) -> None:
        self.movie_data = movie_data

    
    def get_movie_data(self) -> dict:
        return self.movie_data


    def set_data(self, key: str, value: str) -> None:
        self.movie_data[key] = value

    
    def get_data(self, key) -> dict:
        return self.movie_data[key]


    def get_movie_or_show(self, imdb_id):
        return self.get_by_imdb_id(self, imdb_id)


