from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests

from models.Omdb import Omdb
from models.Scraper import Scraper
from database.resourceModels.Search import Search
from database.helpers.Data import DataHelper


app = Flask(__name__)
CORS(app)


OMDB = Omdb()
SCRAPER = Scraper()
DATA_HELPER = DataHelper()
# SEARCH = Search()


@app.route('/api/movify/v1/home', methods=['GET'])
def home():
    SCRAPER.init()
    return {
        'data': 'to-do'
    }

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
    SCRAPER.init()
    return {
        'top_movies': SCRAPER.get_top_movies(10),
        'top_shows': SCRAPER.get_top_shows(10),
        'popular_movies': SCRAPER.get_most_popular_movies(10),
        'popular_shows': SCRAPER.get_most_popular_shows(10),
        'movies_by_genre': SCRAPER.get_genres_ids_from_html()
    }

