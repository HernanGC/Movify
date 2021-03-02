from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests

import json

from models.Omdb import Omdb
from models.Scraper import Scraper
from models.Movies import Movies
from database.resourceModels.Search import Search
from database.helpers.Data import DataHelper


app = Flask(__name__)
CORS(app)


OMDB = Omdb()
# MOVIES = Scraper()
DATA_HELPER = DataHelper()
MOVIES = Movies()
# SEARCH = Search()


@app.route('/api/movify/v1/home', methods=['GET'])
def home():
    MOVIES.init()
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
    res_data = get_json_file_data()
    if not res_data:
        MOVIES.init()
        write_to_file = {}
        write_to_file['top_movies'] = MOVIES.get_top_movies()
        write_to_file['top_shows'] = MOVIES.get_top_shows()
        write_to_file['popular_movies'] = MOVIES.get_most_popular_movies()
        write_to_file['popular_shows'] = MOVIES.get_most_popular_shows()
        write_to_file['movies_by_genre'] = MOVIES.get_genres_ids_from_html()
        set_json_file_data(write_to_file)
        res_data = get_json_file_data()
    set_data(res_data)
    return {
        'data': res_data,
        'data-2': MOVIES.get_most_popular_movies(),
        'movie_data': MOVIES.load_movies()
    }

