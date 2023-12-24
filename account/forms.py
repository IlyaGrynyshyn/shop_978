from django import forms
from account.models import Customer
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(UserCreationForm):
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
        if Customer.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                f'Даний номер телефону вже зареєстрований'
            )
        return phone

    def clean(self):
        password = self.cleaned_data['password1']
        confirm_password = self.cleaned_data['password1']
        if password != confirm_password:
            raise forms.ValidationError('Паролі не співпадають')
        return self.cleaned_data

    class Meta:
        model = Customer
        fields = ('username', 'email', 'first_name', 'phone', 'password1', 'password2')
