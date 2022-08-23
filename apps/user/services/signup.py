# Rest-Framework
from rest_framework.response import Response
from rest_framework import status

# Models
from user.models import User


def signup(username: str, email: str, phone_number: str, password):
    check_phone = User.objects.filter(phone_number=phone_number).exists()
    if check_phone is True:
        return Response({'detail': 'phone already exists'}, status=status.HTTP_400_BAD_REQUEST)
    check_username = User.objects.filter(username=username).exists()
    if check_username is True:
        return Response({'detail': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = create_user(username, email, phone_number, password=password)
    return Response({'detail': 'successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        username: str,
        email: str,
        phone_number: str,
        password=None
):
    user = User.objects.create(
        email=email,
        phone_number=phone_number,
        username=username,
        is_active=False,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.set_password(password)
        user.save()
    return user
