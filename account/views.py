from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, ListView
from django.contrib.auth import views, logout

from account.forms import CustomerRegistrationForm
from account.models import Customer
from utils.services import get_filter_objects, all_objects
from cart.services import Cart
from mainapp.models import TopCategory
from orders.models import Order, OrderItem


class LogoutUserView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("home"))


class CustomerLoginView(views.LoginView):
    """
    View for customer login.
    """
    success_url = reverse_lazy("account:profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class CustomerRegistrationView(FormView):
    """
    View for customer registration.
    """
    form_class = CustomerRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    View for customer profile details.
    """
    model = Customer
    template_name = 'account/profile.html'

    def get_object(self, queryset=None):
        return self.request.user.username

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    """
    View for displaying the order history of a logged-in user.
    """
    model = Order
    template_name = 'account/order_history.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = Order.objects.filter(customer=self.request.user)
        context = super().get_context_data(object_list=object_list, **kwargs)
        order = get_filter_objects(Order, customer=self.request.user)
        order_item = get_filter_objects(OrderItem, order__in=order)
        context['order'] = order
        context['order_item'] = order_item
        context['top_category'] = all_objects(TopCategory)
        context['cart'] = Cart(self.request)
        return context
