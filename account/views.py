from django.contrib.auth.views import LoginView

class LoginCustomView(LoginView):
    template_name = "account/login.html"


