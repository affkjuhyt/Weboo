from __future__ import absolute_import, unicode_literals

import environ

environ.Env.read_env("environments.env")

from .base import *
from .apps import *
from .database import *
from .middleware import *
# from .celery import *
from .log import *
from .email import *
from .restfw import *
from .drf_jwt import *
from .registration import *
from .i18n import *
# from .ethereum import *
# from .influxdb import *
# from .firebase import *
# from .trading_bot import *
# from .matching_engine import *
# from .market_maker import *
# from .defender import *
from .swagger import *
from .django_rq import *
# from .ripple import *

if not ENVIRONMENT == "dev":
    from .production import *
else:
    from .development import *

from celery_worker import app as celery_app

__all__ = ('celery_app',)
