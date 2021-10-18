import os
from .base import BASE_DIR
from django.utils.translation import ugettext_lazy as _

USE_I18N = True

LANGUAGES = (
    ('en', _('English')),
    ('vi', _('VietNam')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
