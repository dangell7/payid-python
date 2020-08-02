network = 'testnet'
# network = 'mainnet'
api_base = 'http://127.0.0.1'
# api_base = 'https://example.com'
api_key = None
api_version = 'v1'
env = 'Prod'
public_port = '8080'
private_port = '8081'

from protocols.payid.resource.base import (  # noqa
    Public,
    Private,
)
