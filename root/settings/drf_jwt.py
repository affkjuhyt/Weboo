import os
import datetime
from django.conf import settings
from root.settings import AUTH_KEYS_DIR

JWT_EXPIRATION_DAYS = int(os.environ.get('JWT_EXPIRATION_DAYS', 30))

JWT_AUTH = {
    'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USERNAME_HANDLER': 'rest_framework_jwt.utils.jwt_get_username_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': 'utils.jwt_util.jwt_get_user_secret_key',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=5),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=6),
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': False if settings.DEBUG else True,
    'JWT_LEEWAY': 0,
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': True,
}
