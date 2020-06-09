api_base = 'https://api.guesty.io'
api_client_id = None
api_client_secret = None
api_version = 'v2'
env = 'Prod'

from guesty.resource.base import (  # noqa
    AccountOAuth,
)

from guesty.resource.property import (  # noqa
    Property,
)
