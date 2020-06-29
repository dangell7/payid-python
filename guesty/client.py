from __future__ import unicode_literals

import requests
import textwrap
# import unicode
from base64 import b64encode

from guesty import api_base, error


def build_url(endpoint):
    url = api_base + '/'

    if endpoint:
        url += endpoint

    return url


def get_env():
    from guesty import env

    if not env:
        raise error.AuthenticationError(
            'No ENV provided. (HINT: set your ENV using '
            '"guesty.env = <DBRef>"). '
        )

    return env


def get_token():
    from guesty import api_client_id, api_client_secret

    if not api_client_id or not api_client_secret:
        raise ValueError('Invalid Client ID or Client Secret')

    return b64encode(bytes(f"{api_client_id}:{api_client_secret}", "utf-8")).decode("ascii")


def get_headers():
    auth_token = get_token()

    if auth_token is None:
        raise error.AuthenticationError(
            'No Auth token provided. (HINT: set your Auth token using '
            '"guesty.auth_token = <AUTH-TOKEN>"). You can generate Auth Tokens keys '
            'from the guesty web interface.'
        )
    return {
        'authorization': 'Basic {}'.format(auth_token),
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }


def put_headers():
    auth_token = get_token()

    if auth_token is None:
        raise error.AuthenticationError(
            'No Auth token provided. (HINT: set your Auth token using '
            '"guesty.auth_token = <AUTH-TOKEN>"). You can generate Auth Tokens keys '
            'from the guesty web interface.'
        )
    return {
        'authorization': 'Basic {}'.format(auth_token),
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }


def get(url, params):
    try:
        # print('Get Url: {}'.format(url))
        # print('Get Params: {}'.format(params))
        res = requests.get(url, params=params, headers=get_headers())
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)


def put(url, json):
    try:
        # print('Put Url: {}'.format(url))
        # print('Put Json: {}'.format(json))
        res = requests.put(url, headers=put_headers(), json=json)
    except Exception as e:
        handle_request_error(e)

    return {'status': res.text}


def delete(url):
    try:
        res = requests.delete(url, headers=headers())
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
        msg = 'Unexpected error communicating with guesty.'
        err = '{}: {}'.format(type(e).__name__, unicode(e))
    else:
        msg = ('Unexpected error communicating with guesty. '
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
    msg = 'Error parsing guesty JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
