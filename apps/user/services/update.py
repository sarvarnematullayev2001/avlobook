from rest_framework import status
from rest_framework.response import Response

from user.models import User


def user_update(user: User, **kwargs):
    for key, value in kwargs.items():
        setattr(user, key, value)
    user.is_new = False
    user.save()
    return Response(
        data={'status': 'Successful updated'},
        status=status.HTTP_200_OK
    )
