from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ..models.otp import OTP
from ..models.user import User
from random import randint


class OTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        mobile = request.data.get('mobile')
        if User.objects.filter(mobile=mobile).exists():
            otp_code = randint(100000, 999999)
            OTP.objects.create(mobile=mobile, otp_code=str(otp_code))
            # In a real system, send the OTP via SMS here
            return Response({"otp_code": otp_code}, status=status.HTTP_201_CREATED)
        return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
