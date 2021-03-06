import json
import requests
from libraries.Response import Response
from flask import Flask, render_template


application = Flask(__name__)


@application.route('/', methods=['GET'])
@application.route('/test', methods=['GET'])
def test_page():
    message = {
        'status': 'Flask up!',
        'pass': 1,
        'fail': 0,
        'testCaseSummaryList': [
            {
                'some key1': 'some value',
                'status': 'key1 status'
            },
            {
                'some key2': 'some value',
                'status': 'key2 status'
            }
        ]
    }
    return application.make_response((json.dumps(message), requests.codes.ok))


@application.route('/health_check', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return application.make_response((json.dumps(message), requests.codes.ok))


@application.route('/pas')
def trigger_pas_regression():
    # response = requests.post('https://test-service.westfield.com/test-run?suite_id=auth_oauth&suite_id=auth_ott')
    #                          'suite_id=account&suite_id=account_app&suite_id=account_credit_cards&suite_id=account_'
    #                          'external_id&suite_id=account_interests&suite_id=account_kids&suite_id=account_loyalty&'
    #                          'suite_id=account_newsletter&suite_id=account_parking&suite_id=account_password&suite_id='
    #                          'account_status&suite_id=account_upgrade&suite_id=account_vehicles&suite_id=people&'
    #                          'suite_id=people_credit_card&suite_id=people_external_ids&suite_id=people_interests&'
    #                          'suite_id=people_kids&suite_id=people_loyalty&suite_id=people_notes&suite_id='
    #                          'people_notifications&suite_id=people_parking&suite_id=people_password_resets&suite_id='
    #                          'people_tickets&suite_id=people_vehicles')
    test_run_id = 1641618757562596763  #response.json()
    response = requests.get(f'https://test-service.westfield.com/test-run?id=1641618757562596763')
    parsed_response = Response().parse_response(response.json())

    # return jsonify(response.json())
    return render_template('pas-test-results.html', initial_response=parsed_response,
                           test_run_id=test_run_id)


if __name__ == '__main__':
    application.run('0.0.0.0', port=5000, debug=True)
