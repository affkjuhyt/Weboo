import logging

import requests
from django.contrib.auth import authenticate
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_registration.api.views.register import RegisterSigner, VerifyRegistrationSerializer
from rest_registration.exceptions import BadRequest
from rest_registration.utils.responses import get_ok_response
from rest_registration.utils.users import get_user_setting, get_user_by_verification_id
from rest_registration.utils.verification import verify_signer_or_bad_request
from validate_email import validate_email
from rest_registration.settings import registration_settings

from authen.serializers.login import LoginSerializer
from userprofile.models import UserProfile
from utils.email import EmailUserNotification

logger = logging.getLogger(__name__.split('.')[0])

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginAPI(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data['username']
        password = request.data['password']
        response = {}
        if validate_email(username):
            email = request.data['username']
            try:
                user_profile = UserProfile.objects.filter(email=email).first()
                user = User.objects.filter(Q(id=user_profile.user.id) | Q(password=password)).first()
            except User.DoesNotExist:
                return Response({'Error': "Invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)

            if user:
                payload = jwt_payload_handler(user)
                jwt_token = jwt_encode_handler(payload)

                response["email"] = user.email
                response["access_token"] = jwt_token

            return Response(response, status=status.HTTP_200_OK)
        else:
            phone_number = request.data['username']

            try:
                user_profile = UserProfile.objects.filter(phone_number=phone_number).first()
                user = User.objects.filter(Q(id=user_profile.user.id) | Q(password=password)).first()
            except User.DoesNotExist:
                return Response({'Error': "Invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)

            if user:
                payload = jwt_payload_handler(user)
                jwt_token = jwt_encode_handler(payload)

                response["email"] = user.email
                response["access_token"] = jwt_token

            return Response(response, status=status.HTTP_200_OK)
