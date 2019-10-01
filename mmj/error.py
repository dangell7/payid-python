class MMJError(Exception):
    def __init__(self, error, status_code=None, headers=None):
        super(MMJError, self).__init__(error)

        self.error = error
        self.status_code = status_code
        self.headers = headers

    def __unicode__(self):
        return self.error


class APIError(MMJError):
    pass


class APIConnectionError(MMJError):
    pass


class InvalidRequestError(MMJError):
    pass


class AuthenticationError(MMJError):
    pass
