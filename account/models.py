from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class Customer(AbstractUser):
    phone = models.CharField(_('phone number'), max_length=30, null=True, blank=True, default="")

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        unique_together = ('username', 'email', 'phone')
