from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests

from models.Request import RequestModel
from database.resourceModels.Search import Search, get_search
from database.helpers.Data import DataHelper


app = Flask(__name__)
CORS(app)


REQUEST_MODEL = RequestModel()
DATA_HELPER = DataHelper()
# SEARCH = Search()


@app.route('/api/movify/v1/search', methods=['GET', 'POST'])
def search_handler():
    if request.method == 'POST':
        data = request.json
        REQUEST_MODEL.set_search_request(data['movie'], 2)
        return jsonify(REQUEST_MODEL.get_response())
    else:
        return 'Hello'


@app.route('/api/movify/v1/test', methods=['GET', 'POST'])
def test_handler():
    if request.method == 'GET':
        res = REQUEST_MODEL.test_request_movie(request.args.get('movie'))
        res_json = res
        return {
            'tv_show_details': REQUEST_MODEL.test_request_details(res_json['Search'][-3]['imdbID']),
            'movie_details': REQUEST_MODEL.test_request_details(res_json['Search'][0]['imdbID']),
            'res': res_json,
        }
    return 'fail'

@app.route('/api/test', methods=['GET', 'POST'])
def test():
    search = REQUEST_MODEL.test_request_movie(request.args.get('movie'))
    REQUEST_MODEL.create_search(search['Search'])
    res = get_search()
    # search = SEARCH.get_search()
    return {
        'obj': 'hello',
        'search': search['Search']
    }

