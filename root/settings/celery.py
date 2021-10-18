import os

from celery.schedules import crontab

CELERY_BROKER_URL = 'redis://{}:{}/{}'.format(os.getenv('REDIS_HOST'),
                                              os.getenv('REDIS_PORT'),
                                              os.getenv('CELERY_REDIS_DB'))

task_routes = {
    'userprofile.tasks.*': {'queue': 'general_task'},
    'wallet.tasks.ethereum_task.*': {'queue': 'ethereum_task'},
    'wallet.tasks.bitcoin_task.*': {'queue': 'bitcoin_task'},
    'wallet.tasks.tron_task.*': {'queue': 'tron_task'}
}

CELERY_BEAT_SCHEDULE = {
    'deposit_eth': {
        'task': 'wallet.tasks.ethereum_task.execute_deposit_eth',
        'schedule': crontab(minute='*/5'),
    },
    'deposit_ethereum_token': {
        'task': 'wallet.tasks.ethereum_task.execute_deposit_ethereum_token',
        'schedule': crontab(minute='*/5'),
    },
    'collect_eth_to_master': {
        'task': 'wallet.tasks.ethereum_task.collect_eth_to_master',
        'schedule': crontab(minute='*/5'),
    },
    'collect_ethereum_token_to_master': {
        'task': 'wallet.tasks.ethereum_task.collect_ethereum_token_to_master',
        'schedule': crontab(minute='*/5'),
    },
    'update_ethereum_address_balance': {
        'task': 'wallet.tasks.ethereum_task.update_ethereum_wallet_address_balance',
        'schedule': crontab(minute='*/5'),
    },
    'withdraw_ethereum': {
        'task': 'wallet.tasks.ethereum_task.withdraw_ethereum',
        'schedule': crontab(minute='*/5'),
    },

    'deposit_btc': {
        'task': 'wallet.tasks.bitcoin_task.execute_deposit_btc',
        'schedule': crontab(minute='*/5'),
    },
    'update_bitcoin_confirmation': {
        'task': 'wallet.tasks.bitcoin_task.update_bitcoin_confirmation',
        'schedule': crontab(minute='*/5'),
    },
    'withdraw_btc': {
        'task': 'wallet.tasks.bitcoin_task.withdraw_bitcoin',
        'schedule': crontab(minute='*/5'),
    },

    'deposit_trx': {
        'task': 'wallet.tasks.tron_task.execute_deposit_trx',
        'schedule': crontab(minute='*/5'),
    },
}
