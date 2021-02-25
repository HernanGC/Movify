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
        self.attrs                 = {'first_attrs': {'class': 'titleColumn'}, 'second_attrs': {'class': 'lister-item-header'}}
        # The "important" movie genres that will be scraped and later rendered in the front end. Might change in the future
        self.important_movies      = ['action', 'adventure', 'comedy', 'documentary', 'family', 'sci-fi', 'thriller', 'western']
        # Top 250 movies scraped from "chart/top/?ref_=nv_mv_250". Set by: "set_top_250_movies()"
        self.top_250_movies        = []
        # Top 250 tv shows scraped from "hart/toptv/?ref_=nv_tvv_250". Set by: "set_top_250_shows()"
        self.top_250_shows         = []
        # Top 100 popular movies scraped from "chart/moviemeter/?ref_=nv_mv_mpm". Set by: "set_most_popular_movies()"
        self.most_popular_movies   = []
        # Top 100 popular tv shows scraped from "chart/tvmeter/?ref_=nv_tvv_mptv". Set by: "set_most_popular_shows() "
        self.most_popular_shows    = []
        # Movie genres URLS scraped from "feature/genre/?ref_=nv_tv_gr". This sets around 50 Movie genres urls, and only 8 are actually used. Set by "set_movie_genres_urls()"
        self.movie_genres_urls     = []
        # Tv Shows genres URLS scraped from "feature/genre/?ref_=nv_tv_gr". This sets around 50 Tv Shows genres urls. Set by "set_shows_genres_urls()"
        self.shows_genres_urls     = []
        # Object composed by "movie_name": "movie_url". Set by "set_movie_genres_object()" in "get_genre_names_from_urls()"
        self.movie_genres          = {}
        # Object composed by "tv_show_name": "tv_show_url".
        self.show_genres           = {}
        # Object composed by "movie_genre": ["imdb_id_one", "imdb_id_two", "..."].
        self.movie_genres_imdb_ids = {}
         

    def init(self):
        '''
        This function initiates the scraper and performs all the scraping needed in order to get the imdbIDs (from imdb.com) for:
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


    def set_movie_genres_urls(self, urls):
        self.movie_genres_urls = urls

    
    def set_shows_genres_urls(self, urls):
        self.shows_genres_urls = urls


    def set_genres_from_html(self):
        genre_list = []
        html = self.get_html(self.MOVIE_SHOWS_GENRES_URL)
        soup = BeautifulSoup(html, 'html.parser')
        genres = soup.find_all(attrs={'class': 'table-cell'})
        for index, genre in enumerate(genres):
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


    def get_genres_ids_from_html(self):
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
            # Get the url from the genre being iterated
            url = self.movie_genres[genre] 
            genre_html = self.get_html(url)
            soup = BeautifulSoup(genre_html, 'html.parser')
            title_results = soup.find_all(attrs={'class': 'lister-item-header'})
            for title in title_results: # Iterate through all the movies to get the imdb_id
                title_href = title.a['href']
                imdb_id = title_href.split('/')[2]
                # Add the id to the list previously initialized as empty in the for loop scope
                imdb_id_list.append(imdb_id)
            self.set_movie_genres_imdb_ids(genre, imdb_id_list) # Set the object's genre key to said genre's imdb_id list
        return self.movie_genres_imdb_ids
    


    def set_movie_genres_imdb_ids(self, genre, imdb_id_list):
        '''
        Sets the "movie_genres_imdb_ids" object given genre as the key and the id list as the value.
        '''
        self.movie_genres_imdb_ids[genre] = imdb_id_list

    
    def set_movie_genres_object(self, movie_title, url):
        '''
        Sets the "movie_genres" object with the given attributes.
        '''
        self.movie_genres[movie_title] = url


    def get_genre_names_from_urls(self, title_urls):
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