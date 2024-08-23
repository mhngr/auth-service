from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from datetime import timedelta
from .models.user import User
from .models.otp import OTP
from .models.login_attemp import LoginAttempt

class AuthenticationTests(APITestCase):

    def setUp(self):
        # Set up initial data for the tests
        self.register_url = reverse('register')
        self.otp_url = reverse('otp')
        self.verify_otp_url = reverse('verify_otp')
        self.login_url = reverse('login')
        self.mobile = "1234567890"
        self.password = "securepassword"

        self.user = User.objects.create_user(
            mobile=self.mobile, password=self.password
        )

    def test_user_registration(self):
        data = {
            "mobile": "0987654321",
            "password": "newpassword",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_otp_generation(self):
        data = {
            "mobile": self.mobile
        }
        response = self.client.post(self.otp_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(OTP.objects.filter(mobile=self.mobile).exists())

    def test_otp_verification(self):
        # Generate OTP first
        otp_code = "123456"
        otp = OTP.objects.create(mobile=self.mobile, otp_code=otp_code)

        # Verify OTP
        data = {
            "mobile": self.mobile,
            "otp_code": otp_code
        }
        response = self.client.post(self.verify_otp_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check OTP is marked as verified
        otp.refresh_from_db()
        self.assertTrue(otp.is_verified)

    def test_user_login_success(self):
        data = {
            "mobile": self.mobile,
            "password": self.password
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_login_failed_attempts_blocking(self):
        # Three failed login attempts
        data = {
            "mobile": self.mobile,
            "password": "wrongpassword"
        }
        for _ in range(3):
            self.client.post(self.login_url, data)

        # The fourth attempt should result in a block
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['error'], "User blocked for 1 hour.")



    def test_ip_based_blocking(self):
        # Simulate three failed attempts from the same IP
        data = {
            "mobile": "nonexistentuser",
            "password": "wrongpassword"
        }
        for _ in range(3):
            self.client.post(self.login_url, data, REMOTE_ADDR='192.168.1.1')

        # The fourth attempt should result in a block
        response = self.client.post(self.login_url, data, REMOTE_ADDR='192.168.1.1')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['error'], "User blocked for 1 hour.")


