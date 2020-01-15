class SmartBnBError(Exception):
    def __init__(self, error, status_code=None, headers=None):
        super(SmartBnBError, self).__init__(error)

        self.error = error
        self.status_code = status_code
        self.headers = headers

    def __unicode__(self):
        return self.error


class APIError(SmartBnBError):
    pass


class APIConnectionError(SmartBnBError):
    pass


class InvalidRequestError(SmartBnBError):
    pass


class AuthenticationError(SmartBnBError):
    pass
