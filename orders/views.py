from django.shortcuts import render
from django.views import View
from cart.services import Cart
from mainapp.models import TopCategory
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from orders.services import all_objects


class OrderCreateView(View):
    """
    View for creating an order.
    """

    def get(self, request):
        cart = Cart(request)
        top_categories = all_objects(TopCategory)
        form = OrderCreateForm()
        return render(
            request,
            'order/checkout.html',
            {'cart': cart, 'form': form, 'top_category': top_categories}
        )

    def post(self, request):
        cart = Cart(request)
        top_categories = all_objects(TopCategory)
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
            return render(request, 'order/success_order.html',
                          {'cart': cart, 'order': order, 'top_category': top_categories})
        return render(request, 'order/checkout.html',
                      {'cart': cart, 'form': form, 'top_category': top_categories})


class SuccessOrderView(View):
    """
      View for successful order placement.
    """

    def get(self, request):
        cart = Cart(request)
        context = {
            'top_category': all_objects(TopCategory),
            'cart': cart
        }
        return render(request, 'order/success_order.html', context)
