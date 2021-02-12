import requests
import json

class RequestHelper:

    API_KEY = 'dffc746e'
    BASE_URL = 'http://www.omdbapi.com/?'

    def __init__(self):
        self.api_key = self.API_KEY
        self.base_url = self.BASE_URL
        self.response = {}

    def set_response(self, res):
        self.response = res
    
    def get_response(self):
        return self.response

    def set_search_request(self, search):
        res = requests.get(f'{self.base_url}s={search}&apikey={self.api_key}')
        self.set_response(json.loads(res.text))

    



    