from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests

import json

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
    res_data = get_json_file_data()
    if not res_data:
        SCRAPER.init()
        write_to_file = {}
        write_to_file['top_movies'] = SCRAPER.get_top_movies()
        write_to_file['top_shows'] = SCRAPER.get_top_shows()
        write_to_file['popular_movies'] = SCRAPER.get_most_popular_movies()
        write_to_file['popular_shows'] = SCRAPER.get_most_popular_shows()
        write_to_file['movies_by_genre'] = SCRAPER.get_genres_ids_from_html()
        set_json_file_data(write_to_file)
        res_data = get_json_file_data()
    set_data(res_data)
    return {
        'data': res_data,
        'data-2': SCRAPER.get_most_popular_movies()
    }


# TODO: Mover esto
def set_json_file_data(data: dict) -> None:
    with open('movies.txt', 'w') as json_file:
        json.dump(data, json_file)

def get_json_file_data() -> dict:
    try:
        with open('movies.txt') as json_file:
            return json.load(json_file)
    except:
        return {}

def set_data(data_dict: dict) -> bool:
    try:
        SCRAPER.set_movie_genres_imdb_ids_obj(data_dict['movies_by_genre'])
        SCRAPER.set_most_popular_movies(data_dict['popular_movies'])
        SCRAPER.set_most_popular_shows(data_dict['popular_shows'])
        SCRAPER.set_top_250_movies(data_dict['top_movies'])
        SCRAPER.set_top_250_shows(data_dict['top_shows'])
        return True
    except:
        return False