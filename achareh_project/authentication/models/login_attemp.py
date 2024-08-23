from django.db import models

"""
The LoginAttempt model tracks login and OTP attempts, storing the mobile number, IP address, timestamp, 
success status, and type (login or otp). This helps implement security measures like blocking after failed attempts.
"""

class LoginAttempt(models.Model):
    mobile = models.CharField(max_length=15, blank=True)
    ip_address = models.CharField(max_length=45, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    attempt_type = models.CharField(max_length=20, choices=[('login', 'login'), ('otp', 'otp')])

    def __str__(self):
        return f"{self.mobile or self.ip_address} - {self.attempt_type} - {self.timestamp}"
