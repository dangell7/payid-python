from __future__ import unicode_literals

import requests
import textwrap

from protocols.payid import (
    network,
    api_base,
    public_port,
    private_port,
    error
)


def build_url(endpoint):
    url = api_base + ':' + public_port + '/'

    if endpoint:
        url += endpoint

    return url


def build_private_url(endpoint):
    url = api_base + ':' + private_port + '/'

    if endpoint:
        url += endpoint

    return url


def get_xrpl_headers():
    if network == 'mainnet':
        return {
            'content-type': 'application/json',
            'PayID-Version': '1.0',
            'accept': 'application/xrpl-mainnet+json'
        }
    return {
        'content-type': 'application/json',
        'PayID-Version': '1.0',
        'accept': 'application/xrpl-testnet+json'
    }


def get_eth_headers():
    if network == 'mainnet':
        return {
            'content-type': 'application/json',
            'PayID-Version': '1.0',
            'accept': 'application/eth-mainnet+json'
        }
    return {
        'content-type': 'application/json',
        'PayID-Version': '1.0',
        'accept': 'application/eth-testnet+json'
    }


def get_all_headers():
    return {
        'content-type': 'application/json',
        'PayID-Version': '1.0',
        'accept': 'application/payid+json'
    }


def get_headers(protocol):
    if protocol == 'xrpl':
        return get_xrpl_headers()
    if protocol == 'eth':
        return get_eth_headers()
    if protocol == 'all':
        return get_all_headers()


def private_headers():
    return {
        'content-type': 'application/json',
        'PayID-API-Version': '2020-06-18'
    }


def patch_headers():
    return {
        'content-type': 'application/merge-patch+json',
        'PayID-API-Version': '2020-06-18'
    }


def get(url, protocol):
    try:
        print('Get Url: {}'.format(url))
        print('Get Protocol: {}'.format(protocol))
        print('Get Headers: {}'.format(get_headers(protocol)))
        res = requests.get(url, headers=get_headers(protocol))
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def private_get(url):
    try:
        print('Get Url: {}'.format(url))
        print('Get Headers: {}'.format(private_headers()))
        res = requests.get(url, headers=private_headers())
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def private_post(url, data):
    try:
        print('Post Url: {}'.format(url))
        print('Post Data: {}'.format(data))
        print('Post Headers: {}'.format(private_headers()))
        res = requests.post(url, headers=private_headers(), json=data)
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def private_put(url, data):
    try:
        print('Put Url: {}'.format(url))
        print('Put Data: {}'.format(data))
        print('Put Headers: {}'.format(private_headers()))
        res = requests.put(url, headers=private_headers(), json=data)
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def private_patch(url, data):
    try:
        print('Patch Url: {}'.format(url))
        print('Patch Data: {}'.format(data))
        print('Patch Headers: {}'.format(private_headers()))
        res = requests.patch(url, headers=patch_headers(), json=data)
        print(res)
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def private_delete(url):
    try:
        res = requests.delete(url, headers=private_headers())
    except Exception as e:
        handle_request_error(e)
    return handle_response(res)


def handle_response(res):
    try:
        json = res.json()
    except ValueError as e:
        handle_parse_error(e)

    if not (199 <= res.status_code < 300):
        handle_error_code(json, res.status_code, res.headers)

    return json


def handle_request_error(e):
    if isinstance(e, requests.exceptions.RequestException):
        msg = 'Unexpected error communicating with PayID.'
        err = '{}: {}'.format(type(e).__name__, str(e))
    else:
        msg = ('Unexpected error communicating with PayID. '
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
    msg = 'Error parsing PayID JSON response. \n\n{}'.format(err)
    raise error.APIError(msg, status_code, headers)
