from django.urls import path
from mainapp.views import BaseListView, CategoryListView

urlpatterns = [
    path("", BaseListView.as_view(), name="home"),
    path('<slug:top_category_slug>/<slug:category_slug>', CategoryListView.as_view(), name='category_detail'),

]