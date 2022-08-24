# Rest-Framework
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Serializers
from user.serializers.signup import SignupSerializer

# Services
from user.services.signup import signup


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return signup(**serializer.validated_data)
