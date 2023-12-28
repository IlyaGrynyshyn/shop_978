from django.shortcuts import render
from django.views import View
from cart.services import Cart
from mainapp.models import TopCategory, Product, Category
from orders.models import OrderItem, Order
from orders.forms import OrderCreateForm


class OrderCreateView(View):
    def get(self, request):
        cart = Cart(request)
        categories = TopCategory.objects.all()
        form = OrderCreateForm()
        return render(request, 'order/checkout.html', {'cart': cart, 'form': form, 'top_category': categories})

    def post(self, request):
        cart = Cart(request)
        categories = TopCategory.objects.all()
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.customer = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'], quantity=item['quantity'])

            cart.clear()
            return render(request, 'order/success_order.html', {'cart': cart, 'order': order, 'top_category': categories})
        return render(request, 'order/checkout.html', {'cart': cart, 'form': form, 'top_category': categories})


class SuccessOrderView(View):
    def get(self, request):
        cart = Cart(request)
        categories = Category.objects.all()
        context = {
            'top_category': TopCategory.objects.all(),
            'cart': cart
        }
        return render(request, 'order/success_order.html', context)
