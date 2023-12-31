import re

from django import forms
from django.core.exceptions import ValidationError

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    """
    Form for creating an order
    """
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'required', 'placeholder': 'Введіть ім\'я'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}))
    midl_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть '
                                                                                                      'по-батькові'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '+38(___)___-____'}))
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form__group'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "Ім'я"
        self.fields['first_name'].empty_label = "Обов'язкове для заповнення"
        self.fields['last_name'].label = 'Прізвище'
        self.fields['last_name'].empty_label = "Обов'язкове для заповнення"
        self.fields['midl_name'].label = 'По-батькові'
        self.fields['phone'].label = 'Номер телефону'
        self.fields['phone'].empty_label = "Обов'язкове для заповнення"
        self.fields['email'].label = "E-mail"
        self.fields['comment'].label = 'Коментарій до замовлення'

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r'^\+38\d{10}$'
        if not re.match(pattern, phone):
            raise ValidationError("Будь ласка, введіть коректний номер телефону у форматі +38(XXX)XXX-XXXX.")
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and not forms.EmailField().clean(email):
            raise ValidationError("Будь ласка, введіть коректну адресу електронної пошти.")
        return email

    class Meta:
        model = Order
        fields = 'first_name', 'last_name', 'midl_name', 'phone', 'email', 'comment'
