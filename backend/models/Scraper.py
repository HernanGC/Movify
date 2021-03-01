import requests
import re
import time
from typing import Union
from bs4 import BeautifulSoup
# from .Request import RequestModel


class Scraper:

    BASE_URL                = 'https://www.imdb.com/'
    MOVIE_SHOWS_GENRES_URL  = 'feature/genre/?ref_=nv_tv_gr'
    TOP_250_SHOWS_URL       = 'chart/toptv/?ref_=nv_tvv_250'
    TOP_250_MOVIES_URL      = 'chart/top/?ref_=nv_mv_250'
    MOST_POPULAR_SHOWS_URL  = 'chart/tvmeter/?ref_=nv_tvv_mptv'
    MOST_POPULAR_MOVIES_URL = 'chart/moviemeter/?ref_=nv_mv_mpm'


    def __init__(self):
        self.attrs: dict                 = {'titleColumn': {'class': 'titleColumn'}, 'lister-item-header': {'class': 'lister-item-header'}}
        # The "important" movie genres that will be scraped and later rendered in the front end. Might change in the future
        self.important_movies: list      = ['action', 'adventure', 'comedy', 'documentary', 'family', 'sci-fi', 'thriller', 'western']
        # Top 250 movies scraped from "chart/top/?ref_=nv_mv_250". Set by: "set_top_250_movies()"
        self.top_250_movies: list        = []
        # Top 250 tv shows scraped from "hart/toptv/?ref_=nv_tvv_250". Set by: "set_top_250_shows()"
        self.top_250_shows: list         = []
        # Top 100 popular movies scraped from "chart/moviemeter/?ref_=nv_mv_mpm". Set by: "set_most_popular_movies()"
        self.most_popular_movies: list   = []
        # Top 100 popular tv shows scraped from "chart/tvmeter/?ref_=nv_tvv_mptv". Set by: "set_most_popular_shows() "
        self.most_popular_shows: list    = []
        # Movie genres URLS scraped from "feature/genre/?ref_=nv_tv_gr". This sets around 50 Movie genres urls, only 8 are actually used. Set by "set_movie_genres_urls()"
        self.movie_genres_urls: list     = []
        # Tv Shows genres URLS scraped from "feature/genre/?ref_=nv_tv_gr". This sets around 50 Tv Shows genres urls. Set by "set_shows_genres_urls()"
        self.shows_genres_urls: list     = []
        # Object composed by "movie_name": "movie_url". Set by "set_movie_genres_object()" in "get_genre_names_from_urls()"
        self.movie_genres: list          = {}
        # Object composed by "tv_show_name": "tv_show_url".
        self.show_genres: list           = {}
        # Object composed by "movie_genre": ["imdb_id_one", "imdb_id_two", "..."].
        self.movie_genres_imdb_ids: dict = {}
         

    def init(self) -> None:
        '''
        This function initializes the scraper and performs all the scraping needed in order to get the imdbIDs (from imdb.com) for:
        - Historic Movie ranking (top 250)
        - Historic Tv Shows ranking (top 250)
        - Current most popular Movies (top 100)
        - Current most popular Tv Shows (top 100)
        - Movies by genres (50 by genre)
        - Tv Shows by genres (50 by genre)
        These ids will later be used to get data from each film from the omdbAPI
        '''
        self.set_most_popular_movies()
        self.set_most_popular_shows()
        self.set_top_250_movies()
        self.set_top_250_shows()
        self.set_genres_from_html()


    def set_top_250_movies(self, movies_dict: dict = None) -> None:
        self.top_250_movies = movies_dict if movies_dict is not None else self.get_top_250(self.TOP_250_MOVIES_URL)

    
    def set_top_250_shows(self, shows_dict: dict = None) -> None:
        self.top_250_shows = shows_dict if shows_dict is not None else self.get_top_250(self.TOP_250_SHOWS_URL)


    def set_most_popular_movies(self, movies_dict: dict = None) -> None:
        self.most_popular_movies = movies_dict if movies_dict is not None else self.get_most_popular(self.MOST_POPULAR_MOVIES_URL)


    def set_most_popular_shows(self, shows_dict: dict = None) -> None:
        self.most_popular_shows = shows_dict if shows_dict is not None else self.get_most_popular(self.MOST_POPULAR_SHOWS_URL)


    def set_movie_genres_urls(self, urls: list) -> None:
        '''Sets the movie genres urls'''
        self.movie_genres_urls = urls

    
    def set_shows_genres_urls(self, urls: list) -> None:
        '''Sets the tv shows genres urls'''
        self.shows_genres_urls = urls


    def set_movie_genres_imdb_ids(self, genre: str, imdb_id_list: str) -> None:
        '''Sets the "movie_genres_imdb_ids" object given genre as the key and the id list as the value.'''
        self.movie_genres_imdb_ids[genre] = imdb_id_list


    def set_movie_genres_imdb_ids_obj(self, imdb_ids_obj: dict) -> None:
        self.movie_genres_imdb_ids = imdb_ids_obj

    
    def set_movie_genres_object(self, movie_title: str, url:str ) -> None:
        '''Sets the "movie_genres" object with the given attributes.'''
        self.movie_genres[movie_title] = url


    def get_top_movies(self, top: int = 250) -> list:
        return self.top_250_movies[:top]


    def get_top_shows(self, top: int = 250) -> list:
        return self.top_250_shows[:top]


    def get_most_popular_movies(self, top: int = 100) -> list:
        return self.most_popular_movies[:top]


    def get_most_popular_shows(self, top: int = 100) -> list:
        return self.most_popular_shows[:top]        


    def get_top_250(self, url: str) -> list:
        html_doc = self.get_html(url)
        top_250_id_list = self.get_imdb_id_from_html(html_doc, self.attrs['titleColumn'])
        return top_250_id_list


    def get_most_popular(self, url: str) -> list:
            html_doc = self.get_html(url)
            most_popular_id_list = self.get_imdb_id_from_html(html_doc, self.attrs['titleColumn'])
            return most_popular_id_list


    def get_html(self, search_url: str) -> str:
        '''Returns the given url html document'''
        return requests.get(self.BASE_URL+search_url).text

    
    def get_imdb_id_from_html(self, html_doc: str, attrs: dict) -> Union[list, bool]:
        '''Returns a list of imdb_id's from the given html document that match the given attributes.'''
        imdb_id_list = []
        try:
            soup = BeautifulSoup(html_doc, 'html.parser')
            title_results = soup.find_all(attrs=attrs)
            for title in title_results:
                title_href = title.a['href']
                imdb_id = title_href.split('/')[2]
                imdb_id_list.append(imdb_id)
            return imdb_id_list
        except:
            return False


    def set_genres_from_html(self) -> list:
        '''Gets and sets the urls for movie and tv shows genres'''
        genre_list = []
        html = self.get_html(self.MOVIE_SHOWS_GENRES_URL)
        soup = BeautifulSoup(html, 'html.parser')
        genres = soup.find_all(attrs={'class': 'table-cell'})
        for index, genre in enumerate(genres):
            # These html elements being skipped are repeated ones, therefor I skip them
            if genre in {genres[0], genres[7], genres[14], genres[21], genres[28], genres[36], genres[44], genres[52]}:
                continue
            elif index < 59:
                genre_url = genre.a['href']
                genre_list.append(genre_url)
            else:
                break
        self.set_movie_genres_urls(genre_list[:24])
        self.set_shows_genres_urls(genre_list[24:])
        return genre_list


    def get_genres_ids_from_html(self) -> dict:
        '''
        Returns and sets the genres imdb_id's for each of the urls that were previously set in the "movie_genres" object by "set_genres_from_html()",
        these urls will only be the ones that match the genres defined in the "important_movies" list.
        '''
        # I get ALL the movie urls that were previously loaded in the "movie_genres_urls" list
        urls_list = self.movie_genres_urls
        # Filter them to get a resulting genres list and create a new object ("movie_genres") 
        # which will contain => "genre": "url" only for those genres I want to
        movie_genre_titles = self.get_genre_names_from_urls(urls_list)
        for genre in movie_genre_titles:
            imdb_id_list = [] # Each iteration this list begins empty
            url = self.movie_genres[genre] # Gets the url from the genre being iterated
            genre_html = self.get_html(url)
            soup = BeautifulSoup(genre_html, 'html.parser')
            imdb_id_list = self.get_imdb_id_from_html(genre_html, self.attrs['lister-item-header']) # Gets a list of the imdb_ids
            if imdb_id_list:
                self.set_movie_genres_imdb_ids(genre, imdb_id_list)
        return self.movie_genres_imdb_ids
    

    def get_genre_names_from_urls(self, title_urls: list) -> list:
        '''
        Returns a list of genre names from the urls list given that match with the "important_movies" list. 
        Also calls the function "set_movie_genres_object()" that the "movie_genres" object with the url and
        the genre name as => "genre": "url".
        '''
        titles = []
        for title in title_urls:
            split_title = title.split('=')[1].split('&')[0]
            if split_title in self.important_movies:
                self.set_movie_genres_object(split_title, title)
                titles.append(split_title)
        return titles
