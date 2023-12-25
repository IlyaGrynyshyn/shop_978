from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.contrib.auth import views, logout

from account.forms import CustomerRegistrationForm
from account.models import Customer


class CustomerLoginView(views.LoginView):
    success_url = reverse_lazy("account:profile")


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


@login_required(login_url="account:login")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("home"))
