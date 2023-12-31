from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from mainapp.models import Product
from cart.services import Cart

class CartAddView(View):
    """
    View for adding a product to the cart.
    """
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        return redirect('cart:cart_detail')

class CartRemoveView(View):
    """
    View for removing a product from the cart.
    """
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')

class AddQuantityView(View):
    """
    View for adding quantity to a product in the cart.
    """
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add_quantity(product)
        return redirect(request.META['HTTP_REFERER'])

class SubtractionQuantityView(View):
    """
    View for subtracting quantity from a product in the cart.
    """
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.subtraction_quantity(product)
        return redirect(request.META['HTTP_REFERER'])

class CartDetailView(View):
    """
    View for displaying cart details.
    """
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})
