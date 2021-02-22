import requests
import re
from bs4 import BeautifulSoup
# from .Request import RequestModel


class Scraper:

    BASE_URL = 'https://www.imdb.com/'
    TOP_250_MOVIES_URL = 'chart/top/?ref_=nv_mv_250'
    MOST_POPULAR_MOVIES_URL = 'chart/moviemeter/?ref_=nv_mv_mpm'
    TOP_250_SHOWS_URL = 'chart/toptv/?ref_=nv_tvv_250'
    MOST_POPULAR_SHOWS_URL = 'chart/tvmeter/?ref_=nv_tvv_mptv'


    def __init__(self):
        self.top_250_movies = []
        self.most_popular_movies = []
        self.top_250_shows = []
        self.most_popular_shows = []


    def get_top_250_movies(self, top=250):
        return self.get_top_250(self.TOP_250_MOVIES_URL, top, self.top_250_movies)

    
    def get_top_250_shows(self, top=250):
        return self.get_top_250(self.TOP_250_SHOWS_URL, top, self.top_250_shows)


    def get_most_popular_movies(self, top=100):
        return self.get_most_popular(self.MOST_POPULAR_MOVIES_URL, top, self.most_popular_movies)


    def get_most_popular_shows(self, top=100):
        return self.get_most_popular(self.MOST_POPULAR_SHOWS_URL, top, self.most_popular_shows)


    def get_top_250(self, url, top, top_list):
        html_doc = self.get_html(url)
        top_250_id_list = self.get_imdb_id_from_html(html_doc, top_list)
        return top_250_id_list[:top]


    def get_most_popular(self, url, top, popular_list):
            html_doc = self.get_html(url)
            most_popular_id_list = self.get_imdb_id_from_html(html_doc, popular_list)
            return most_popular_id_list[:top]


    def get_html(self, search_url):
        return requests.get(self.BASE_URL+search_url).text

    
    def get_imdb_id_from_html(self, html_doc, list_el):
        imdb_id_list = []
        try:
            attrs = {'class': 'titleColumn'}
            soup = BeautifulSoup(html_doc, 'html.parser')
            title_results = soup.find_all(attrs=attrs)
            for title in title_results:
                title_href = title.a['href']
                imdb_id = title_href.split('/')[2]
                list_el.append(imdb_id)
            return list_el
        except:
            return False


