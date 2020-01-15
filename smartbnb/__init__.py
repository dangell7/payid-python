api_base = 'https://api.smartbnb.io'
api_client_id = None
api_client_secret = None
api_version = 'v2'
env = 'Prod'

from smartbnb.resource.base import (  # noqa
    AccountOAuth,
)

from smartbnb.resource.property import (  # noqa
    Property,
)
