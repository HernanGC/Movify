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
        self.attrs               = {'first_attrs': {'class': 'titleColumn'}, 'second_attrs': {'class': 'lister-item-header'}}
        self.top_250_movies      = []
        self.top_250_shows       = []
        self.most_popular_movies = []
        self.most_popular_shows  = []
        self.movie_genres_urls   = []
        self.shows_genres_urls   = []
        self.important_movies    = ['action', 'adventure', 'comedy', 'documentary', 'family', 'sci-fi', 'thriller', 'western']
        self.movie_genres        = {}
        self.movie_genres_two    = {}
        self.show_genres         = {}


    def get_genres_ids_from_html(self):
        imdb_id_list = []
        self.set_genres_from_html()
        urls_list = self.movie_genres_urls
        movie_genre_titles = self.get_genre_names_from_urls(urls_list)
        for genre in movie_genre_titles:
            imdb_id_list = []
            url = self.movie_genres[genre]
            genre_html = self.get_html(url)
            soup = BeautifulSoup(genre_html, 'html.parser')
            title_results = soup.find_all(attrs={'class': 'lister-item-header'})
            for title in title_results:
                title_href = title.a['href']
                imdb_id = title_href.split('/')[2]
                print('---')
                print(imdb_id)
                imdb_id_list.append(imdb_id)
            self.movie_genres_two[genre] = imdb_id_list
        return self.movie_genres_two
    
    
    def get_genre_names_from_urls(self, title_urls):
        titles = []
        for title in title_urls:
            split_title = title.split('=')[1].split('&')[0]
            if split_title in self.important_movies:
                self.movie_genres[split_title] = title
                titles.append(split_title)
        return titles
         

    def init(self):
        self.set_most_popular_movies()
        self.set_most_popular_shows()
        self.set_top_250_movies()
        self.set_top_250_shows()


    def set_top_250_movies(self, top=250):
        self.top_250_movies = self.get_top_250(self.TOP_250_MOVIES_URL)

    
    def set_top_250_shows(self, top=250):
        self.top_250_shows = self.get_top_250(self.TOP_250_SHOWS_URL)


    def set_most_popular_movies(self, top=100):
        self.most_popular_movies = self.get_most_popular(self.MOST_POPULAR_MOVIES_URL)


    def set_most_popular_shows(self, top=100):
        self.most_popular_shows = self.get_most_popular(self.MOST_POPULAR_SHOWS_URL)


    def get_top_movies(self, top):
        return self.top_250_movies[:top]


    def get_top_shows(self, top):
        return self.top_250_shows[:top]


    def get_most_popular_movies(self, top):
        return self.most_popular_movies[:top]


    def get_most_popular_shows(self, top):
        return self.most_popular_shows[:top]        


    def get_top_250(self, url):
        html_doc = self.get_html(url)
        top_250_id_list = self.get_imdb_id_from_html(html_doc, self.attrs['first_attrs'])
        return top_250_id_list


    def get_most_popular(self, url):
            html_doc = self.get_html(url)
            most_popular_id_list = self.get_imdb_id_from_html(html_doc, self.attrs['first_attrs'])
            return most_popular_id_list


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


    def set_genres_from_html(self):
        genre_list = []
        html = self.get_html(self.MOVIE_SHOWS_GENRES_URL)
        soup = BeautifulSoup(html, 'html.parser')
        genres = soup.find_all(attrs={'class': 'table-cell'})
        index = 0
        # TODO: Refactor this to a pythonic for loop using enumarate()
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


    # def set    