from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ..models.login_attemp import LoginAttempt
from ..models.user import User
from ..serializers.user_login_serializer import UserLoginSerializer
from django.utils import timezone
from datetime import timedelta

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data['mobile']
            password = serializer.validated_data['password']
            user = User.objects.filter(mobile=mobile).first()

            if user and user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)

            # Log failed login attempt
            ip_address = request.META.get('REMOTE_ADDR', '')
            LoginAttempt.objects.create(mobile=mobile, ip_address=ip_address, success=False, attempt_type='login')

            # Check if the IP should be blocked
            recent_attempts = LoginAttempt.objects.filter(
                ip_address=ip_address,
                success=False,
                attempt_type='login',
                timestamp__gt=timezone.now() - timedelta(hours=1)
            )

            if recent_attempts.count() >= 3:
                return Response({"error": "User blocked for 1 hour."}, status=status.HTTP_403_FORBIDDEN)

            return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
