import requests
import json

class RequestHelper:

    API_KEY = 'dffc746e'
    BASE_URL = 'http://www.omdbapi.com/?'
 
    def __init__(self):
        self.api_key = self.API_KEY
        self.base_url = self.BASE_URL
        self.response = []

    def set_response(self, res):
        self.response += res
    
    def get_response(self):
        return self.response

    def set_search_request(self, search, pages):
        for page in range(int(pages)):
            try:
                response = requests.get(f'{self.base_url}s={search}&page={page+1}&apikey={self.api_key}').json()
                print(response)
                if (response['Response'] == 'True'):
                    self.set_response(response['Search'])
            except (KeyError, ValueError):
                print('ERROR EN LA REQUEST A LA API!')
            
        

    



    