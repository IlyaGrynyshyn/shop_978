from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class Customer(AbstractUser):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
        null=True,
        blank=True
    )
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"
