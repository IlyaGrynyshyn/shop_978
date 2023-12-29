from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import CustomerRegistrationView, ProfileDetailView, CustomerLoginView, logout_user, OrderHistoryView

app_name = 'account'

urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', CustomerRegistrationView.as_view(), name='registration'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('order_history/', OrderHistoryView.as_view(), name='order_history')
]
