from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

Roles = (("admin","admin"), ("creator","creator"), ("sale","sale"))

class CustomUserManager(BaseUserManager):
    def create_superuser(self, eamail, password,**extra_fields ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superviser must Have is_staff=True.")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superviser must Have is_superuser=True.")

        if not eamail:
            raise ValueError("Email Field is required")

        user =  self.model(eamail=eamail, **extra_fields)
        user.set_password(password)
        user.save()

        return user 



