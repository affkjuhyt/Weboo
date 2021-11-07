from rest_framework.exceptions import APIException


class APIError(APIException):
    status_code = 400
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'api_error'


class APIException(Exception):
    def __init__(self, code=201, message='API weirdo', args=('API weirdo',)):
        self.args = args
        self.code = code
        self.message = message

    def __str__(self):
        return self.message


class GenException(APIException):
    pass
