from rest_framework.response import Response


class SuccessResponse(Response):
    """
    SuccessResponse(data)
    (1) return 200
    """

    def __init__(self, data=None, msg='success', status=None, template_name=None, headers=None, exception=False,
                 content_type=None):
        self.std_data = {
            "code": 200,
            "data": data,
            "msg": msg,
            "status": 'success'
        }
        super().__init__(self.std_data, status, template_name, headers, exception, content_type)

    def __str__(self):
        return str(self.std_data)


class ErrorResponse(Response):
    """
    ErrorResponse(msg='xxx')
    (1) return 201, ErrorResponse(code=xxx)
    """

    def __init__(self, data=None, msg='error', code=201, status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        self.std_data = {
            "code": code,
            "data": data,
            "msg": msg,
            "status": 'error'
        }
        super().__init__(self.std_data, status, template_name, headers, exception, content_type)

    def __str__(self):
        return str(self.std_data)
