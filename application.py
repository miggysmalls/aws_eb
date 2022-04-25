import json
import requests
from flask import Flask


application = Flask(__name__)


@application.route('/')
@application.route('/health_check', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return application.make_response((json.dumps(message), requests.codes.ok))


if __name__ == '__main__':
    application.run('0.0.0.0', port=5000, debug=True)
