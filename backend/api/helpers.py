import requests
import json

class RequestHelper:

    API_KEY = 'dffc746e'
    BASE_URL = 'http://www.omdbapi.com/?'
    SEARCH_TYPES = {

    }

    def __init__(self):
        self.api_key = self.API_KEY
        self.base_url = self.BASE_URL
        self.response = []

    def set_response(self, res):
        self.response += res
        print(f'ACA ${self.response}')
    
    def get_response(self):
        return self.response

    def set_search_request(self, search, pages):
        for page in range(int(pages)):
            self.set_response(requests.get(f'{self.base_url}s={search}&page={page+1}&apikey={self.api_key}').json()['Search'])
        

    



    