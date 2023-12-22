from django.urls import path
from mainapp.views import BaseListView

urlpatterns = [
    path("", BaseListView.as_view(), name="home")
]