from __future__ import unicode_literals

import requests
import textwrap
import json

from airbnb import api_base, api_version, error

def build_url(endpoint):
    url = api_base + api_version + '/'

    if endpoint:
        url += endpoint

    return url

def get_env():
    from airbnb import env

    if not env:
        raise error.AuthenticationError(
            'No ENV provided. (HINT: set your ENV using '
            '"airbnb.env = <DBRef>"). '
        )

    return env

def get_token():
    from airbnb import api_username, api_password

    if not api_username or not api_password:
        raise ValueError('Invalid UserName or Password')

    BASE_URL = 'https://api.airbnb.com/v2/logins'
    payload = {
        'email': api_username,
        'password': api_password,
    }

    # Client ID does NOT change
    params = {
        'client_id': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
        'currency': 'USD',
    }
    return 'cnkhpnmm7ql2zlv5mjvsmmvo0'
    # res = requests.post(BASE_URL, params=params, json=payload, headers=get_auth_headers())
    # print(res)
    # print(res.text)
    # data = json.loads(res.text)
    # return data['login']['id']

def get_auth_headers():
    return {
        'X-Airbnb-OAuth-Token': '',
        'X-Airbnb-Device-Id': '12345678231',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

def get_headers(auth_token):
    if auth_token is None:
        raise error.AuthenticationError(
            'No Auth token provided. (HINT: set your Auth token using '
            '"airbnb.auth_token = <AUTH-TOKEN>"). You can generate Auth Tokens keys '
            'from the AirBnB web interface.'
        )
    return {
        'X-Airbnb-OAuth-Token': auth_token,
        'X-Airbnb-Device-Id': '12345678231',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

def post_headers():

    return {
        'Content-Type': 'text/plain',
        'Accept': 'application/json'
    }

def get(url, params):
    try:
        print('Get Url: {}'.format(url))
        print('Get Params: {}'.format(params))
        res = requests.get(url, params=params, headers=get_headers('cnkhpnmm7ql2zlv5mjvsmmvo0'))
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)

def post(url, json):
    try:
        # print('Post Url: {}'.format(url))
        res = requests.post(url, headers=post_headers(), json=json)
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)


def delete(url):
    try:
        res = requests.delete(url, headers=get_headers())
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)

def handle_response(res):
    try:
        res.raise_for_status()
        json = res.json()
    except ValueError as e:
        handle_parse_error(e)

    if not (200 <= res.status_code < 300):
        handle_error_code(json, res.status_code, res.headers)

    return json

def handle_request_error(e):
    if isinstance(e, requests.exceptions.RequestException):
        msg = 'Unexpected error communicating with AirBnB.'
        err = '{}: {}'.format(type(e).__name__, unicode(e))
    else:
        msg = ('Unexpected error communicating with AirBnB. '
               'It looks like there\'s probably a configuration '
               'issue locally.')
        err = 'A {} was raised'.format(type(e).__name__)
        if u'%s' % e:
            err += ' with error message {}'.format(e)
        else:
            err += ' with no error message'

    msg = textwrap.fill(msg) + '\n\n(Network error: {})'.format(err)
    raise error.APIConnectionError(msg)

def handle_error_code(json, status_code, headers):
    if status_code == 400:
        err = json.get('error', 'Bad request')
        raise error.InvalidRequestError(err, status_code, headers)
    elif status_code == 401:
        err = json.get('error', 'Not authorized')
        raise error.AuthenticationError(err, status_code, headers)
    elif status_code == 404:
        err = json.get('error', 'Not found')
        raise error.InvalidRequestError(err, status_code, headers)
    elif status_code == 500:
        err = json.get('error', 'Internal server error')
        raise error.APIError(err, status_code, headers)
    else:
        err = json.get('error', 'Unknown status code ({})'.format(status_code))
        raise error.APIError(err, status_code, headers)

def handle_parse_error(e, status_code=None, headers=None):
    err = '{}: {}'.format(type(e).__name__, e)
    msg = 'Error parsing AirBnB JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
