import os

from .base import DEBUG

APPS_THROTTLE_GET_REQUEST = os.environ.get("APPS_THROTTLE_GET_REQUEST", 100)
APPS_THROTTLE_POST_REQUEST = os.environ.get("APPS_THROTTLE_POST_REQUEST", 10)
APPS_THROTTLE_PUT_REQUEST = os.environ.get("APPS_THROTTLE_PUT_REQUEST", 10)
APPS_THROTTLE_PATCH_REQUEST = os.environ.get("APPS_THROTTLE_PATCH_REQUEST", 10)
APPS_THROTTLE_DELETE_REQUEST = os.environ.get("APPS_THROTTLE_DELETE_REQUEST", 10)
APPS_THROTTLE_DURATION_REQUEST = os.environ.get("APPS_THROTTLE_DURATION_REQUEST", 'minute')

DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'utils.base_pagination.BasePageNumberPagination',
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'util.jwt.jwt_response_payload_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'utils.base_throttle.RequestMethodThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user_get': '%s/%s' % (APPS_THROTTLE_GET_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_post': '%s/%s' % (APPS_THROTTLE_POST_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_put': '%s/%s' % (APPS_THROTTLE_PUT_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_patch': '%s/%s' % (APPS_THROTTLE_PATCH_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
        'user_delete': '%s/%s' % (APPS_THROTTLE_DELETE_REQUEST, APPS_THROTTLE_DURATION_REQUEST),
    },

    'SOCIAL_AUTH_PIPELINE': (
        'social_core.pipeline.social_auth.social_details',
        'social_core.pipeline.social_auth.social_uid',
        'social_core.pipeline.social_auth.auth_allowed',
        'social_core.pipeline.social_auth.social_user',
        'social_core.pipeline.user.get_username',
        'social_core.pipeline.social_auth.associate_by_email',
        'social_core.pipeline.user.create_user',
        'social_core.pipeline.social_auth.associate_user',
        'social_core.pipeline.social_auth.load_extra_data',
        'social_core.pipeline.user.user_details',)
}
