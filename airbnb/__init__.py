api_base = 'https://api.airbnb.com/'
api_username = None
api_password = None
api_version = 'v2'
env = 'Prod'

from airbnb.resource.base import (  # noqa
    Account,
)

from airbnb.resource.property import (  # noqa
    Property,
)
