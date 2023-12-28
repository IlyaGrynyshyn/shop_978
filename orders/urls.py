from django.urls import path
from orders.views import OrderCreateView,SuccessOrderView

app_name = 'order'

urlpatterns = [
    path('checout/', OrderCreateView.as_view(), name='order_create'),
    path('success-order/', SuccessOrderView.as_view(), name='success_order')
]
