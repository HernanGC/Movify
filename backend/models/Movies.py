from typing import Union
from .Omdb import Omdb

class Movies(Omdb):
    

    def __init__(self):
        self.movies_data: dict  = {}


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

    
    def load_movies(self):
        top_movies = self.get_top_movies(15)
        popular_movies = self.get_most_popular_movies(15)
        top_movies_list = []
        popular_movies_list = []
        for index, movie in enumerate(top_movies):
            print(movie)
            top_movies_list.append(self.get_movie_by_imdb_id(movie))
            popular_movies_list.append(self.get_movie_by_imdb_id(popular_movies[index]))
        self.movie_data['top_movies'] = top_movies_list
        self.movie_data['popular_movies'] = popular_movies_list
        return self.movie_data



