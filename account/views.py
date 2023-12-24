from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView

from account.forms import CustomerRegistrationForm
from account.models import Customer


class CustomerRegistrationView(FormView):
    form_class = CustomerRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model=Customer
    template_name = 'account/profile.html'

    def get_object(self, queryset=None):
        return self.request.user.username




