from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ..models.otp import OTP
from django.core.exceptions import ObjectDoesNotExist


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        mobile = request.data.get('mobile')
        otp_code = request.data.get('otp_code')
        try:
            otp = OTP.objects.get(mobile=mobile, otp_code=otp_code, is_verified=False)
            otp.is_verified = True
            otp.save()
            return Response({"message": "OTP verified successfully."}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
