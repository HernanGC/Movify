import requests
import json

from database.resourceModels.Search import Search
from database.base import sess


class Omdb:


    API_KEY = 'dffc746e'
    BASE_URL = 'http://www.omdbapi.com/?'
 

    def __init__(self):
        self.api_key = self.API_KEY
        self.base_url = self.BASE_URL
        self.response = []

    
    def get_request(self, url):
        res = requests.get(url)
        return res.status_code


    def set_response(self, res):
        '''
        Set the request response
        '''
        self.response += res
    

    def get_response(self):
        '''
        Get the request response
        '''
        return self.response


    def set_search_request(self, search, pages):
        '''
        Set search, currently implemented for 2 pages, this needs refactor to make it dynamic and adapt the program flow
        '''
        for page in range(int(pages)):
            try:
                response = requests.get(f'{self.base_url}s={search}&page={page+1}&apikey={self.api_key}').json()
                print(response)
                if (response['Response'] == 'True'):
                    self.set_response(response['Search'])
            except (KeyError, ValueError):
                print('ERROR EN LA REQUEST A LA API!')

    
    # Testing functions
    
    def test_request_movie(self, movie_name):
        '''
        Get search results
        '''
        return requests.get(f'{self.base_url}s={movie_name}&apikey={self.api_key}').json()


    def test_request_details(self, movie_id):
        '''
        Get details result
        '''
        return requests.get(f'{self.base_url}i={movie_id}&apikey={self.api_key}').json()
            

    def create_search(self, obj):
        sess.rollback()
        for i in obj:
            search = Search(i['Title'], i['Type'], i['Year'], i['imdbID'], i['Poster'])
            sess.add(search)
            sess.commit()
            sess.close()

    



    