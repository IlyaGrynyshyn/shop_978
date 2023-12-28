from django.urls import path
from cart.views import CartDetailView, CartAddView, CartRemoveView, AddQuantityView, SubtractionQuantityView

app_name = 'cart'

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),
    path('add_qty/<int:product_id>/', AddQuantityView.as_view(), name='change_qty'),
    path('subtraction_quantity/<int:product_id>/', SubtractionQuantityView.as_view(), name='subtraction_quantity')
]
