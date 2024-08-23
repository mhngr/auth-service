from django.db import models

"""
The OTP model stores OTP codes sent to users, including the mobile number, OTP code, creation time, 
and verification status. It helps manage OTP-based authentication by tracking whether the OTP is verified.
"""


class OTP(models.Model):
    mobile = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mobile} - {self.otp_code}"
