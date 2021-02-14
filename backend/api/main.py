from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
import sys, requests
from helpers import RequestHelper
# from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/api/movify/v1/search', methods=['GET', 'POST'])
def search_handler():
    if request.method == 'POST':
        data = request.json
        request_helper = RequestHelper()
        request_helper.set_search_request(data['movie'], 2)
        # print()
        print(request_helper.get_response())
        return jsonify(request_helper.get_response())
    else:
        return 'Hello'

