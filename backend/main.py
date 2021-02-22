from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests

from models.Omdb import Omdb
from models.Scraper import Scraper
from database.resourceModels.Search import Search, get_search
from database.helpers.Data import DataHelper


app = Flask(__name__)
CORS(app)


OMDB = Omdb()
SCRAPER = Scraper()
DATA_HELPER = DataHelper()
# SEARCH = Search()


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
    return {
        'obj': SCRAPER.get_most_popular()
    }

