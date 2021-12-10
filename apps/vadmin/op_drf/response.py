"""
Response Django Response、DRF Response
"""
from django.http.response import DjangoJSONEncoder, JsonResponse
from rest_framework.response import Response


class OpDRFJSONEncoder(DjangoJSONEncoder):
    """
    DjangoJSONEncoder
    (1) json
    """

    def __init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False,
                 indent=None, separators=None, default=None):
        super().__init__(skipkeys=skipkeys, ensure_ascii=False, check_circular=check_circular,
                         allow_nan=allow_nan, sort_keys=sort_keys, indent=indent, separators=separators,
                         default=default)


class SuccessResponse(Response):
    """
    SuccessResponse(data) SuccessResponse(data=data)
    (1) 200
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
    (1) 201, ErrorResponse(code=xxx)
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


class SuccessJsonResponse(JsonResponse):
    """
    JsonResponse, SuccessJsonResponse(data)SuccessJsonResponse(data=data)
    (1)仅SuccessResponse SuccessJsonResponse
    """

    def __init__(self, data, msg='success', encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs):
        std_data = {
            "code": 200,
            "data": data,
            "msg": msg,
            "status": 'success'
        }
        super().__init__(std_data, encoder, safe, json_dumps_params, **kwargs)


class ErrorJsonResponse(JsonResponse):
    """
    JsonResponse, ErrorResponse, ErrorJsonResponse
    (1) 2001, ErrorJsonResponse(code=xxx)
    """

    def __init__(self, data, msg='error', code=201, encoder=OpDRFJSONEncoder, safe=True, json_dumps_params=None,
                 **kwargs):
        std_data = {
            "code": code,
            "data": data,
            "msg": msg,
            "status": 'error'
        }
        super().__init__(std_data, encoder, safe, json_dumps_params, **kwargs)
