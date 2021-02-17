from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import sys, requests
from helpers import RequestHelper

app = Flask(__name__)
CORS(app)

@app.route('/api/movify/v1/search', methods=['GET', 'POST'])
def search_handler():
    if request.method == 'POST':
        data = request.json
        request_helper = RequestHelper()
        request_helper.set_search_request(data['movie'], 2)
        return jsonify(request_helper.get_response())
    else:
        return 'Hello'

