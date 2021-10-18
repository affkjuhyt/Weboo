import os

from root.settings import EMAIL_NOTIFICATION_SENDER

FRONTEND_ROOT_URL = os.environ.get("APPS_FRONTEND_ROOT_URL")

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_URL': '{}/active'.format(FRONTEND_ROOT_URL),
    'RESET_PASSWORD_VERIFICATION_URL': '{}/forgot'.format(FRONTEND_ROOT_URL),
    'USER_EMAIL_FIELD': 'email',
    'USER_VERIFICATION_FLAG_FIELD': 'is_active',
    'REGISTER_VERIFICATION_ENABLED': True,
    'VERIFICATION_FROM_EMAIL': EMAIL_NOTIFICATION_SENDER,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
    'REGISTER_SERIALIZER_CLASS': 'authen.serializers.register.RegisterSerializer',
    'REGISTER_VERIFICATION_EMAIL_TEMPLATES': {
        'subject': 'rest_registration/register/subject.txt',
        'body': 'rest_registration/register/body.txt',
        'html': 'email/verify_registration.html'
    },
    'RESET_PASSWORD_VERIFICATION_EMAIL_TEMPLATES': {
        'subject': 'rest_registration/reset_password/subject.txt',
        'body': 'rest_registration/reset_password/body.txt',
        'html': 'email/notify_reset_password.html'
    },
}
