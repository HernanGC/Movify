import requests
import re
from bs4 import BeautifulSoup
# from .Request import RequestModel


class Scraper:

    BASE_URL = 'https://www.imdb.com/'
    TOP_250_URL = 'chart/top/?ref_=nv_mv_250'
    MOST_POPULAR_URL = 'chart/moviemeter/?ref_=nv_mv_mpm'


    def __init__(self):
        self.top_250 = []
        self.most_popular = []


    def get_top_250(self, top=250):
        html_doc = self.get_html(self.TOP_250_URL)
        top_250_id_list = self.get_imdb_id_from_html(html_doc, self.top_250)
        return top_250_id_list[:top]


    def get_html(self, search_url):
        return requests.get(self.BASE_URL+search_url).text


    def get_most_popular(self, top=100):
        html_doc = self.get_html(self.MOST_POPULAR_URL)
        most_popular_id_list = self.get_imdb_id_from_html(html_doc, self.most_popular)
        return most_popular_id_list[:top]

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


