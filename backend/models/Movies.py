from .Omdb import Omdb

class Movies(Omdb):
    

    def __init__(self):
        self.imdb_id     = ''
        self.title       = ''
        self.year        = ''
        self.released    = ''
        self.actors      = ''
        self.awards      = ''
        self.box_office  = ''
        self..director   = ''
        self.genre       = ''
        self.language    = ''
        self.metascore   = ''
        self.plot        = ''
        self.poster      = ''
        self.rated       = ''
        self.response    = ''
        self.runtime     = ''
        self.writer      = ''
        self.imdb_rating = ''


    def get_movie_or_show(self, imdb_id):
        # TODO: Hacer un setter que procese y setee la data pertinente
        return self.get_by_imdb_id(self, imdb_id)


    def set_data(self, key, value):
        self.key = value
