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

from userprofile.models import UserProfile
from utils.email import EmailUserNotification

logger = logging.getLogger(__name__.split('.')[0])

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

FACEBOOK_DEBUG_TOKEN_URL = "https://graph.facebook.com/debug_token"
FACEBOOK_ACCESS_TOKEN_URL = "https://graph.facebook.com/v7.0/oauth/access_token"
FACEBOOK_URL = "https://graph.facebook.com/"


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        try:
            user = User.objects.get(last_name=data['email'])
        except User.DoesNotExist:
            user = User()
            user.last_name = data['email']
            user.username = data['email']
            user.password = make_password(BaseUserManager().make_random_password())
            user.save()

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response["user_id"] = user.id
        response['username'] = user.username
        response['access_token'] = str(token)
        return Response(response)


class FacebookView(APIView):
    def post(self, request):
        user_info_url = FACEBOOK_URL + request.data.get("id")
        print(request.data.get("id"), request.data.get("token"))
        user_info_payload = {
            "access_token": request.data.get("token"),
        }

        user_info_request = requests.get(user_info_url, params=user_info_payload)
        user_info_response = json.loads(user_info_request.text)

        try:
            user = User.objects.get(last_name=user_info_response["id"])
        except User.DoesNotExist:
            user = User()
            user.last_name = user_info_response["id"]
            user.username = user_info_response["id"]
            user.password = make_password(BaseUserManager().make_random_password())
            user.save()

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response["user_id"] = user.id
        response["username"] = user.username
        response["access_token"] = str(token)
        return Response(response)


class AppleView(APIView):
    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide user_id"}, status=status.HTTP_400_BAD_REQUEST)

        user_name = request.data.get("user_id")

        try:
            user = User.objects.get(last_name=user_name)
        except User.DoesNotExist:
            user = User()
            user.last_name = user_name
            user.username = user_name
            user.password = make_password(BaseUserManager().make_random_password())
            user.save()

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response["username"] = user.username
        response["user_id"] = user.id
        response["access_token"] = str(token)
        return Response(response, status=status.HTTP_200_OK)
