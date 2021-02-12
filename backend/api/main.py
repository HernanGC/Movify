from flask import Flask, request
import sys, requests
from helpers import RequestHelper
# from flask import request

app = Flask(__name__)

@app.route('/api/movify/v1/search', methods=['GET', 'POST'])
def search_handler():
    if request.method == 'POST':
        data = request.json
        print(data)
        print(data['movie'])
        request_helper = RequestHelper()
        request_helper.set_search_request(data['movie'])
        return request_helper.get_response()

