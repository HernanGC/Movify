from typing import Union
from . import Omdb

class Movies(Omdb.Omdb):
    

    def __init__(self):
        self.movies_data: dict  = {}
        super().__init__()


    def set_movie_data(self, movie_data: dict) -> None:
        self.movie_data = movie_data

    
    def get_movie_data(self) -> dict:
        return self.movie_data


    def set_data(self, key: str, value: str) -> None:
        self.movie_data[key] = value

    
    def get_data(self, key) -> Union[str, list, dict]:
        return self.movie_data[key]


    def get_movie_by_imdb_id(self, imdb_id: str) -> dict:
        return self.get_by_imdb_id(imdb_id, 'movie')

    
    def load_movies(self, top_movies_qty: int = 250, popular_movies_qty: int = 100):
        # TODO: Hacer esto como la funcion load_tv_shows()
        top_movies = self.get_top_movies(top_movies_qty)
        popular_movies = self.get_most_popular_movies(popular_movies_qty)
        top_movies_list = []
        popular_movies_list = []
        for index, movie in enumerate(top_movies):
            top_movies_list.append(self.get_movie_by_imdb_id(movie))
            if index < 100: popular_movies_list.append(self.get_movie_by_imdb_id(popular_movies[index])) 
        self.movies_data['top_movies'] = top_movies_list
        self.movies_data['popular_movies'] = popular_movies_list
        return self.movies_data

    
    def load_movies_by_genre(self):
        pass



