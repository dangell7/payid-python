class guestyError(Exception):
    def __init__(self, error, status_code=None, headers=None):
        super(guestyError, self).__init__(error)

        self.error = error
        self.status_code = status_code
        self.headers = headers

    def __unicode__(self):
        return self.error


class APIError(guestyError):
    pass


class APIConnectionError(guestyError):
    pass


class InvalidRequestError(guestyError):
    pass


class AuthenticationError(guestyError):
    pass
