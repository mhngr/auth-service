from django.db import models


class LoginAttempt(models.Model):
    mobile = models.CharField(max_length=15, blank=True)
    ip_address = models.CharField(max_length=45, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    attempt_type = models.CharField(max_length=20, choices=[('login', 'login'), ('otp', 'otp')])

    def __str__(self):
        return f"{self.mobile or self.ip_address} - {self.attempt_type} - {self.timestamp}"
