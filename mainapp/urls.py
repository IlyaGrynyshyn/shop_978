from django.urls import path
from mainapp.views import BaseListView, CategoryListView, ProductDetailView

urlpatterns = [
    path("", BaseListView.as_view(), name="home"),
    path('product/<slug:product_slug>', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:top_category_slug>/<slug:category_slug>', CategoryListView.as_view(), name='category_detail')

]
