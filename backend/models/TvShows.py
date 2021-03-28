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
        return self.get_by_imdb_id(imdb_id, 'series')

    def load_tv_shows(self, tv_shows_qty: int = 15) -> dict:
        self.show_data = list(map(self.get_show_by_imdb_id, self.get_most_popular_shows(tv_shows_qty)))
        return self.show_data
