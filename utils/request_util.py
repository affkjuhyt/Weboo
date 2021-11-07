"""
Request util
"""
import logging

from django.core.cache import cache
from user_agents import parse

from root.settings import base

logger = logging.getLogger(__name__)


def get_browser(request, *args, **kwargs):
    """
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    ua_string = request.META['HTTP_USER_AGENT']
    user_agent = parse(ua_string)
    return user_agent.get_browser()


def get_request_ip(request):
    """
    Request IP
    :param request:
    :return:
    """
    ip = getattr(request, 'request_ip', None)
    if ip:
        return ip
    ip = request.META.get('REMOTE_ADDR', '')
    if not ip:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = 'unknown'
    return ip


def get_login_location(request, *args, **kwargs):
    """
    Request location
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    if not getattr(base, "ENABLE_LOGIN_LOCATION", False): return ""
    import requests
    import eventlet
    request_ip = get_request_ip(request)
    location = cache.get(request_ip) if getattr(base, "REDIS_ENABLE", False) else ""
    if location:
        return location
    try:
        eventlet.monkey_patch(thread=False)  # 必须加这条代码
        with eventlet.Timeout(2, False):  # 设置超时时间为2秒
            apiurl = "http://whois.pconline.com.cn/ip.jsp?ip=%s" % request_ip
            r = requests.get(apiurl)
            content = r.content.decode('GBK')
            location = str(content).replace('\r', '').replace('\n', '')[:64]
            if getattr(base, "REDIS_ENABLE", False):
                cache.set(request_ip, location, 86400)
            return location
    except Exception as e:
        pass
    return ""


def get_os(request, *args, **kwargs):
    """
    Request OS
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    ua_string = request.META['HTTP_USER_AGENT']
    user_agent = parse(ua_string)
    return user_agent.get_os()
