import logging
import uuid
from base64 import b32encode
from decimal import Decimal, ROUND_DOWN
from os import urandom

import requests


logger = logging.getLogger(__name__.split('.')[0])


def get_clean_phone_number(phone_number):
    clean_mobile = phone_number.strip()
    if clean_mobile.startswith('+84'):
        clean_mobile = clean_mobile.replace('+84', '0')
    if clean_mobile.startswith('84'):
        clean_mobile = clean_mobile.replace('84', '0')
    elif not clean_mobile.startswith('0'):
        clean_mobile = '0%s' % clean_mobile
    return clean_mobile


def generate_code(digits=6):
    return uuid.uuid4().hex[:digits].upper()


def random_token():
    """
    Returns a new random string that can be used as a static token.

    :rtype: str
    """
    return b32encode(urandom(5)).decode('utf-8').lower()


def round_amount(amount, prec=8):
    amount = amount if isinstance(amount, Decimal) else Decimal(amount)
    fmt = '.{}1'.format(
        '0' * (prec - 1)
    )
    return amount.quantize(Decimal(fmt), rounding=ROUND_DOWN)
