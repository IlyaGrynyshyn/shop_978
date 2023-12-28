from decimal import Decimal
from django.conf import settings
from mainapp.models import Product


class Cart:

    def __init__(self, request) :
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        print(str(product.id))
        print('im here')
        self.save()

    def add_quantity(self, product):
        product_id = str(product.id)
        self.cart[product_id]['quantity'] += 1
        self.save()

    def subtraction_quantity(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] == 1:
                del self.cart[product_id]
            else:
                self.cart[product_id]['quantity'] -= 1
        self.save()

    def save(self):
        """
        Mark the session as "modified" to make sure it gets saved
        """
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        calculate the total cost of the items in the cart
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def sum_of_product(self, product):
        product_id = str(product.id)
        return sum(item['quantity'] * item['price'] for item in self.cart.key(product_id))

    def get_total_item(self):
        """
        Calculate the total item of the items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Remove cart from session
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
