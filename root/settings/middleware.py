import datetime
import json
import logging

from django.db import connection
from django.utils.deprecation import MiddlewareMixin
from user_agents import parse

logger = logging.getLogger(__name__.split('.')[0])


class GetUserAgentMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_agent = parse(request.META.get("HTTP_USER_AGENT", ""))
        request.middleware_user_agent = user_agent


class RequestMonitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info('START---------------------------------------')
        request.start_time = datetime.datetime.utcnow()

    def process_response(self, request, response):
        # Enable if want to log all queries (DEBUG) in 1 transfer
        # if connection.queries:
        #     for query in connection.queries:
        #         logger.debug(query)
        api_detail = f'"{request.method} {request.path}" {response.status_code}'
        if response.status_code != 200:
            try:
                api_detail = f'{api_detail} {json.loads(response.content.decode()).get("detail", "")}'
            except Exception:
                pass
        logger.info(api_detail)
        logger.info(f'API took {(datetime.datetime.utcnow() - request.start_time).microseconds / 1000} ms')
        logger.info('-----------------------------------------END')
        return response


MIDDLEWARE = [
    'root.settings.middleware.RequestMonitorMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'defender.middleware.FailedLoginMiddleware',
    'root.settings.middleware.GetUserAgentMiddleware',
]
