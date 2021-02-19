from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests
from helper import RequestHelper


app = Flask(__name__)
CORS(app)


REQUEST_HELPER = RequestHelper()


@app.route('/api/movify/v1/search', methods=['GET', 'POST'])
def search_handler():
    if request.method == 'POST':
        data = request.json
        REQUEST_HELPER.set_search_request(data['movie'], 2)
        return jsonify(REQUEST_HELPER.get_response())
    else:
        return 'Hello'


@app.route('/api/movify/v1/test', methods=['GET', 'POST'])
def test_handler():
    if request.method == 'GET':
        res = REQUEST_HELPER.test_request_movie(request.args.get('movie'))
        res_json = res
        return {
            'tv_show_details': REQUEST_HELPER.test_request_details(res_json['Search'][-3]['imdbID']),
            'movie_details': REQUEST_HELPER.test_request_details(res_json['Search'][0]['imdbID']),
            'res': res_json,
        }
    return 'fail'

