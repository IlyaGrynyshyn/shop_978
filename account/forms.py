import re

from django import forms
from account.models import Customer
from django.contrib.auth.forms import UserCreationForm


class CustomerRegistrationForm(UserCreationForm):
    """
    Form for customer registration.
    """
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email', max_length=255, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(label='First Name', max_length=255, required=False)
    phone = forms.CharField(label='Phone Number', max_length=30, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Дана пошта вже зареєстрована'
            )
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r'^\+38\d{10}$'
        if not re.match(pattern, phone):
            raise forms.ValidationError("Будь ласка, введіть коректний номер телефону у форматі +38(XXX)XXX-XXXX.")
        if Customer.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                f'Даний номер телефону вже зареєстрований'
            )
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Паролі не співпадають')

        return cleaned_data

    class Meta:
        model = Customer
        fields = ('username', 'email', 'first_name', 'phone', 'password1', 'password2')
