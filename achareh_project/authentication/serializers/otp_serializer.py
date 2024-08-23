from rest_framework import serializers
from ..models.otp import OTP


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['mobile', 'otp_code']