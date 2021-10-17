from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _
from rest_framework.views import exception_handler
from rest_registration.exceptions import BadRequest


def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        try:
            if isinstance(exc.args[0], dict):
                return exception_handler(BadRequest(_(list(exc.args[0].values())[0][0])), context)
            else:
                return exception_handler(BadRequest(_(exc.args[0])), context)
        except Exception:
            return exception_handler(exc, context)
    return exception_handler(exc, context)
