from random import randint

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from user.models import VerifyUser, User
from user.services.sms import send_phone_sms_code


def send_user_verify_code(user, is_forgot_password=False):
    code = randint(100_000, 999_999)
    if is_forgot_password is False:
        VerifyUser.objects.create(
            user=user,
            code=f'verify_username_{code}',
            is_active=False
        )
    elif is_forgot_password is True:
        VerifyUser.objects.create(
            user=user,
            code=f'forgot_password_{code}',
            is_active=False
        )
    send_phone_sms_code(user.username, code)


def check_verify_signup_code(username, code):
    check = VerifyUser.objects.filter(
        user__username=username,
        code=f'verify_username_{code}',
        is_active=False
    )
    if check.exists():
        verify = check.first()
        verify.is_active = True
        verify.save()
        user = verify.user
        user.is_active = True
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)


def check_verify_forgot_password_code(username, code):
    check = VerifyUser.objects.filter(
        user__username=username,
        code=f'forgot_password_{code}',
        is_active=False
    )
    return check.exists()


def re_send_verify_user_code(username):
    try:
        user = User.objects.get(username=username)
        send_user_verify_code(user)
        return Response({'detail': 'successfully send new code'})
    except User.DoesNotExist:
        return Response({'detail': 'username does not exist'}, status=status.HTTP_400_BAD_REQUEST)
