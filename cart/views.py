from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from mainapp.models import Product
from cart.services import Cart

class CartAddView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        return redirect('cart:cart_detail')

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')

class AddQuantityView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add_quantity(product)
        return redirect(request.META['HTTP_REFERER'])

class SubtractionQuantityView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.subtraction_quantity(product)
        return redirect(request.META['HTTP_REFERER'])

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})
