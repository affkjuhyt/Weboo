import os
from os.path import join

from root.settings import BASE_DIR

LOGFILE_ROOT = os.environ.get("APPS_LOGFILE_ROOT") if os.environ.get("APPS_LOGFILE_ROOT") else BASE_DIR
MAX_BYTES = 10485760

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '%(asctime)s %(levelname)s (%(name)s - %(filename)s:%(lineno)d) - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(LOGFILE_ROOT, 'main_debug.log'),
            'maxBytes': MAX_BYTES,  # 5 MB
            'formatter': 'main_formatter',
            'backupCount': 7,
        }
    },
    'loggers': {
        'root': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'authentication': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'market': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'userprofile': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'util': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'wallet': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
    }
}