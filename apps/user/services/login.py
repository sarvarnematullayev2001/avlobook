# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Django
from django.contrib.auth import authenticate

# Project
from user.models import User
from user.services.verify import re_send_verify_user_code


def login(username: str, password, is_superuser=False):
    invalid_username_or_password = 'invalid_username_or_password'
    activate_error = 'please_activate_your_account'

    try:
        user = User.objects.get(username=username)
        if user.is_active is False:
            re_send_verify_user_code(username)
            return Response({'detail': activate_error}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response({'detail': invalid_username_or_password}, status=status.HTTP_400_BAD_REQUEST)
        if is_superuser is True and user.is_superuser is False:
            return Response({'detail': 'access denied'}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    except User.DoesNotExist:
        return Response({'detail': invalid_username_or_password}, status=status.HTTP_400_BAD_REQUEST)
