from typing import Union
from . import Omdb

class TvShows(Omdb.Omdb):


    def __init__(self):
        self.shows_data: dict = {}
        super().__init__()


    def set_show_data(self, show_data: dict) -> None:
        self.show_data = show_data

    
    def get_show_data(self) -> dict:
        return self.show_data


    def set_data(self, key: str, value: str) -> None:
        self.show_data[key] = value

    
    def get_data(self, key: str) -> Union[str, list, dict]:
        return self.show_data[key]


    def get_show_by_imdb_id(self, imdb_id: str) -> dict:
        return self.get_by_imdb_id(imdb_id)


    # def load_shows(self):
