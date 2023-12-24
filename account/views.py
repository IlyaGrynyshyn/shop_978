from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from account.forms import CustomerRegistrationForm


class CustomerRegistrationView(FormView):
    form_class = CustomerRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)

