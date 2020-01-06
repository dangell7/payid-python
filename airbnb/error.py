class AirBnBError(Exception):
    def __init__(self, error, status_code=None, headers=None):
        super(AirBnBError, self).__init__(error)

        self.error = error
        self.status_code = status_code
        self.headers = headers

    def __unicode__(self):
        return self.error


class APIError(AirBnBError):
    pass


class APIConnectionError(AirBnBError):
    pass


class InvalidRequestError(AirBnBError):
    pass


class AuthenticationError(AirBnBError):
    pass
