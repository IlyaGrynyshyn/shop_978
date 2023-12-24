from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import CustomerRegistrationView, ProfileDetailView

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(success_url="account:profile"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', CustomerRegistrationView.as_view(), name='registration'),
    path('profile/', ProfileDetailView.as_view(), name='profile')
]
