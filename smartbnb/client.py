from __future__ import unicode_literals

import requests
import textwrap
import json

from smartbnb import api_base, error

def build_url(endpoint):
    url = api_base + '/'

    if endpoint:
        url += endpoint

    return url

def get_env():
    from smartbnb import env

    if not env:
        raise error.AuthenticationError(
            'No ENV provided. (HINT: set your ENV using '
            '"smartbnb.env = <DBRef>"). '
        )

    return env

def get_bearer_token():
    from smartbnb import api_client_id, api_client_secret, api_base

    if not api_client_id or not api_client_secret:
        raise error.AuthenticationError(
            'No Client ID or Secret provided. (HINT: set your Client ID and Secret using '
            '"smartbnb.api_client_ID = <CLIENT_ID/API_KEY>"). You can generate Client ID and Secret pair keys '
            'from the SmartBnB web interface.'
        )

    BASE_URL = 'https://auth.smartbnb.io/oauth/token'
    payload = {
        'client_id': api_client_id,
        'client_secret': api_client_secret,
        'audience': 'api.smartbnb.io',
        'grant_type': 'client_credentials'
    }

    auth_headers = {
        'Content-Type': 'application/json',
    }

    try:
        res = requests.post(BASE_URL, json=payload, headers=auth_headers)
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)

def headers(auth_token):
    if auth_token is None:
        raise error.AuthenticationError(
            'No Auth token provided. (HINT: set your Auth token using '
            '"smartbnb.auth_token = <AUTH-TOKEN>"). You can generate Auth Tokens keys '
            'from the SmartBnB web interface.'
        )
    return {
        'authorization': 'Bearer {}'.format(auth_token),
        'accept': 'application/json',
        'content-type': 'application/vnd.smartbnb.20191201+json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

def put_headers(auth_token):
    if auth_token is None:
        raise error.AuthenticationError(
            'No Auth token provided. (HINT: set your Auth token using '
            '"smartbnb.auth_token = <AUTH-TOKEN>"). You can generate Auth Tokens keys '
            'from the SmartBnB web interface.'
        )
    return {
        'authorization': 'Bearer {}'.format(auth_token),
        'accept': 'application/json',
        'content-type': 'application/vnd.smartbnb.20191231+json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

def get(auth_token, url, params):
    try:
        # print('Get Token: {}'.format(auth_token))
        # print('Get Url: {}'.format(url))
        # print('Get Params: {}'.format(params))
        res = requests.get(url, params=params, headers=headers(auth_token))
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)

def put(auth_token, url, params, json):
    try:
        print('Get Token: {}'.format(auth_token))
        print('Put Url: {}'.format(url))
        print('Put Params: {}'.format(params))
        print('Put Json: {}'.format(json))
        res = requests.put(url, params=params, headers=put_headers(auth_token), json=json)
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
        msg = 'Unexpected error communicating with SmartBnB.'
        err = '{}: {}'.format(type(e).__name__, unicode(e))
    else:
        msg = ('Unexpected error communicating with SmartBnB. '
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
    msg = 'Error parsing SmartBnB JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
