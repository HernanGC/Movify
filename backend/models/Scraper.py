import requests
import re
import time
from bs4 import BeautifulSoup
# from .Request import RequestModel


class Scraper:

    BASE_URL = 'https://www.imdb.com/'
    TOP_250_MOVIES_URL = 'chart/top/?ref_=nv_mv_250'
    TOP_250_SHOWS_URL = 'chart/toptv/?ref_=nv_tvv_250'
    MOST_POPULAR_MOVIES_URL = 'chart/moviemeter/?ref_=nv_mv_mpm'
    MOST_POPULAR_SHOWS_URL = 'chart/tvmeter/?ref_=nv_tvv_mptv'
    MOVIE_SHOWS_GENRES_URL = 'feature/genre/?ref_=nv_tv_gr'



    def __init__(self):
        self.attrs = {'first_attrs': {'class': 'titleColumn'}, 'second_attrs': {'class': 'lister-item-header'}}
        self.top_250_movies = []
        self.top_250_shows = []
        self.most_popular_movies = []
        self.most_popular_shows = []
        self.movie_genres_urls = []
        self.shows_genres_urls = []


    def init(self):
        self.set_most_popular_movies(10)
        self.set_most_popular_shows(10)
        self.set_top_250_movies(10)
        self.set_top_250_shows(10)


    def set_top_250_movies(self, top=250):
        self.top_250_movies = self.get_top_250(self.TOP_250_MOVIES_URL, top)

    
    def set_top_250_shows(self, top=250):
        self.top_250_shows = self.get_top_250(self.TOP_250_SHOWS_URL, top)


    def set_most_popular_movies(self, top=100):
        self.most_popular_movies = self.get_most_popular(self.MOST_POPULAR_MOVIES_URL, top)


    def set_most_popular_shows(self, top=100):
        self.most_popular_shows = self.get_most_popular(self.MOST_POPULAR_SHOWS_URL, top)


    def get_top_movies(self):
        return self.top_250_movies


    def get_top_shows(self):
        return self.top_250_shows


    def get_most_popular_movies(self):
        return self.most_popular_movies


    def get_most_popular_shows(self):
        return self.most_popular_shows        


    def get_top_250(self, url, top):
        html_doc = self.get_html(url)
        top_250_id_list = self.get_imdb_id_from_html(html_doc, self.attrs['first_attrs'])
        return top_250_id_list[:top]


    def get_most_popular(self, url, top):
            html_doc = self.get_html(url)
            most_popular_id_list = self.get_imdb_id_from_html(html_doc, self.attrs['first_attrs'])
            return most_popular_id_list[:top]


    def get_html(self, search_url):
        return requests.get(self.BASE_URL+search_url).text

    
    def get_imdb_id_from_html(self, html_doc, attrs):
        imdb_id_list = []
        try:
            curr_attrs = attrs
            soup = BeautifulSoup(html_doc, 'html.parser')
            title_results = soup.find_all(attrs=curr_attrs)
            for title in title_results:
                title_href = title.a['href']
                imdb_id = title_href.split('/')[2]
                imdb_id_list.append(imdb_id)
            return imdb_id_list
        except:
            return False


    def get_genres_from_html(self):
        genre_list = []
        html = self.get_html(self.MOVIE_SHOWS_GENRES_URL)
        soup = BeautifulSoup(html, 'html.parser')
        genres = soup.find_all(attrs={'class': 'table-cell'})
        index = 0
        for genre in genres:
            index += 1
            if genre in {genres[0], genres[7], genres[14], genres[21], genres[28], genres[36], genres[44], genres[52]}:
                continue
            elif index < 59:
                genre_url = genre.a['href']
                genre_list.append(genre_url)
            else:
                break
        self.movie_genres_urls = genre_list[:24]
        self.shows_genres_urls = genre_list[24:]
        return genre_list