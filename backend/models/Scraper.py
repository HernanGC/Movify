import requests
import re
from bs4 import BeautifulSoup
# from .Request import RequestModel


class Scraper:

    BASE_URL = 'https://www.imdb.com/'
    TOP_250_URL = 'chart/top/?ref_=nv_mv_250'


    def __init__(self):
        self.top_250 = []
        # self.req = RequestModel()


    def get_top_250(self, top=250):
        html_doc = self.get_top_250_html()
        self.process_html(html_doc)
        return self.top_250[:top]


    def get_top_250_html(self):
        return requests.get(self.BASE_URL+self.TOP_250_URL).text


    def process_html(self, html_doc):
        try:
            attrs = {'class': 'titleColumn'}
            soup = BeautifulSoup(html_doc, 'html.parser')
            title_results = soup.find_all(attrs=attrs)
            for title in title_results:
                title_href = title.a['href']
                imdb_id = title_href.split('/')[2]
                self.top_250.append(imdb_id)
            return True
        except:
            return False


