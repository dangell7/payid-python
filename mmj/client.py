from __future__ import unicode_literals

import requests
import textwrap

from mmj import api_base, api_version, error

def build_url(endpoint):
    url = api_base + api_version + '/'

    if endpoint:
        url += endpoint

    return url

def get_env():
    return env

def get_headers():
    from mmj import api_key

    if api_key is None:
        raise error.AuthenticationError(
            'No API key provided. (HINT: set your API key using '
            '"mmj.api_key = <API-KEY>"). You can generate API keys '
            'from the MMJ web interface.'
        )

    return {
        'Api-Key': api_key,
        'Content-Type': 'application/json'
    }

def get(url):
    try:
        print('Get Url: {}'.format(url))
        res = requests.get(url, headers=get_headers())
    except Exception as e:
        handle_request_error(e)

    return handle_response(res)

def post(url, json):
    try:
        print('Post Url: {}'.format(url))
        res = requests.post(url, headers=get_headers(), json=json)
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
        json = res.json()
    except ValueError as e:
        handle_parse_error(e)

    if not (200 <= res.status_code < 300):
        handle_error_code(json, res.status_code, res.headers)

    return json


def handle_request_error(e):
    if isinstance(e, requests.exceptions.RequestException):
        msg = 'Unexpected error communicating with MMJ.'
        err = '{}: {}'.format(type(e).__name__, unicode(e))
    else:
        msg = ('Unexpected error communicating with MMJ. '
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
    err = '{}: {}'.format(type(e).__name__, unicode(e))
    msg = 'Error parsing MMJ JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
