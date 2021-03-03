from flask import Flask, request, jsonify
from flask_cors import CORS

import sys, requests, json

from models.Omdb import Omdb
from models.Scraper import Scraper
from models.Movies import Movies
from models.Main import Main

from database.resourceModels.Search import Search
from database.helpers.Data import DataHelper


app = Flask(__name__)
CORS(app)


MAIN = Main()
OMDB = Omdb()
# MOVIES = Scraper()
DATA_HELPER = DataHelper()
MOVIES = Movies()
# SEARCH = Search()


@app.route('/api/movify/v1/home', methods=['GET'])
def home():
    return MAIN.initializeF()

@app.route('/api/movify/v1/search', methods=['GET', 'POST'])
def search_handler():
    if request.method == 'POST':
        data = request.json
        OMDB.set_search_request(data['movie'], 2)
        return jsonify(OMDB.get_response())
    else:
        return 'Hello'


@app.route('/api/movify/v1/test', methods=['GET', 'POST'])
def test_handler():
    if request.method == 'GET':
        res = OMDB.test_request_movie(request.args.get('movie'))
        res_json = res
        return {
            'tv_show_details': OMDB.test_request_details(res_json['Search'][-3]['imdbID']),
            'movie_details': OMDB.test_request_details(res_json['Search'][0]['imdbID']),
            'res': res_json,
        }
    return 'fail'

@app.route('/api/test', methods=['GET', 'POST'])
def test():
    return MAIN.initializeF()

