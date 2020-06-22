api_base = 'https://api.guesty.com/api/v2'
api_client_id = None
api_client_secret = None
api_version = 'v2'
env = 'Prod'

from guesty.resource.base import (  # noqa
    Account,
)

from guesty.resource.listing import (  # noqa
    Listing,
)
