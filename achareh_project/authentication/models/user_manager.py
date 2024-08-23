from django.contrib.auth.models import  BaseUserManager

"""
The UserManager class customizes user creation, requiring a mobile number.
It includes methods to create users . This supports mobile-based authentication.
"""


class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError("The Mobile field must be set")
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


