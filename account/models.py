from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class Customer(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"