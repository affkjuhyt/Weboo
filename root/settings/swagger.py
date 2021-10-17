SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Authorization': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
    },
    'USE_SESSION_AUTH': True,
}
