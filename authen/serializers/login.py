from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.compat import Serializer
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_registration.exceptions import BadRequest

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER


class LoginSerializer(JSONWebTokenSerializer):
    # def validate(self, attrs):
    #     username = attrs.get(self.username_field)
    #     if '@' in username:
    #         user = User.objects.filter(email=username, is_active=True).first()
    #         if user:
    #             username = user.username
    #     credentials = {
    #         self.username_field: username,
    #         'password': attrs.get('password')
    #     }
    #
    #     if not all(credentials.values()):
    #         raise BadRequest(_(f'Must include "{self.username_field}" and "password".'))
    #     user = authenticate(**credentials)
    #     if not user:
    #         raise BadRequest(_('Unable to login with provided credentials.'))
    #     if not user.is_active:
    #         raise BadRequest(_('User account is disabled.'))
    #     if user.userprofile.is_two_factor_enabled:
    #         return {
    #             'is_two_factor_enabled': user.userprofile.is_two_factor_enabled,
    #             'user_id': user.id
    #         }
    #     payload = jwt_payload_handler(user)
    #     return {
    #         'token': jwt_encode_handler(payload),
    #         'user': user
    #     }

    def update(self, instance, validated_data):
        raise NotImplementedError('Not supported')

    def create(self, validated_data):
        raise NotImplementedError('Not supported')

