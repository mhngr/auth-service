from django.urls import path
from .views.user_registration_view import UserRegistrationView
from .views.otp_view import OTPView
from .views.verify_otp_view import VerifyOTPView
from .views.user_login_view import UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('otp/', OTPView.as_view(), name='otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('login/', UserLoginView.as_view(), name='login'),
]
