from rest_framework import status
from rest_framework.response import Response

from user.models import User, VerifyUser
from user.services.verify import send_user_verify_code, check_verify_forgot_password_code


def send_forgot_password_code(username: str):
    try:
        user = User.objects.get(username=username)
        send_user_verify_code(user, is_forgot_password=True)
        return Response({'detail': 'successfully'})
    except User.DoesNotExist:
        return Response({'detail': 'username does not exists'}, status=status.HTTP_400_BAD_REQUEST)


def check_forgot_password_code(username: str, code: str):
    return Response({'status': check_verify_forgot_password_code(username, code)})


def set_new_password(username: str, code: str, new_password: str):
    try:
        check_code = check_verify_forgot_password_code(username, code)
        if check_code is False:
            return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        VerifyUser.objects.filter(
            user__username=username,
            code=f'forgot_password_{code}',
            is_active=False
        ).update(is_active=True)
        return Response({'detail': 'successfully'})
    except User.DoesNotExist:
        return Response({'detail': 'username does not exists'}, status=status.HTTP_400_BAD_REQUEST)

