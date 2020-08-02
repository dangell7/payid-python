class PayIDError(Exception):
    def __init__(self, error, status_code=None, headers=None):
        super(PayIDError, self).__init__(error)

        self.error = error
        self.status_code = status_code
        self.headers = headers

    def __unicode__(self):
        return self.error


class APIError(PayIDError):
    pass


class APIConnectionError(PayIDError):
    pass


class InvalidRequestError(PayIDError):
    pass


class AuthenticationError(PayIDError):
    pass
