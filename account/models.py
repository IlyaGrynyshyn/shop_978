from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
