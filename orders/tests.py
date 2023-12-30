from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from orders.forms import OrderCreateForm
from orders.models import Order


class OrderCreateFormTest(TestCase):

    def test_valid_data(self):
        form_data = {
            'first_name': 'Test First name',
            'last_name': 'Test Last name',
            'midl_name': 'Test Midl Name',
            'phone': '+380991234567',
            'email': 'test@example.com',
            'comment': 'Test comment'
        }
        form = OrderCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_required_field(self):
        form_data = {
            'last_name': 'Test Last name',
            'midl_name': 'Test Midl Name',
            'phone': '+380991234567',
            'email': 'test@example.com',
            'comment': 'Test comment'
        }
        form = OrderCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_invalid_phone(self):
        form_data = {
            'first_name': 'Test Last name',
            'last_name': 'Test Last name',
            'midl_name': 'Test Midl Name',
            'phone': '123',
            'email': 'test@mail.com',
            'comment': 'Test comment'
        }
        form = OrderCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_invalid_email(self):
        form_data = {
            'first_name': 'Test Last name',
            'last_name': 'Test Last name',
            'midl_name': 'Test Midl Name',
            'phone': '+380991234567',
            'email': 'testmain.com',
            'comment': 'Test comment'
        }
        form = OrderCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_clean_phone_with_valid_data(self):
        form_data = {
            'first_name': 'Test Last name',
            'last_name': 'Test Last name',
            'midl_name': 'Test Midl Name',
            'phone': '+380991234567',
            'email': 'test@mail.com',
            'comment': 'Test comment'
        }
        form = OrderCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        cleaned_phone = form.clean_phone()
        self.assertEqual(cleaned_phone, '+380991234567')

    def test_clean_email_with_valid_data(self):
        form_data = {
            'first_name': 'Test First name',
            'last_name': 'Test Last name',
            'midl_name': 'Test Midl Name',
            'phone': '+380991234567',
            'email': 'test@mail.com',
            'comment': 'Test comment'
        }
        form = OrderCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        cleaned_email = form.clean_email()
        self.assertEqual(cleaned_email, 'test@mail.com')


class OrderCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@mail.com',
                                                         password='password')

    def test_get_request(self):
        url = reverse('order:order_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/checkout.html')
        self.assertIn('cart', response.context)
        self.assertIn('form', response.context)
        self.assertIn('top_categories', response.context)

    def test_post_request_valid_data_unauthenticated_user(self):
        data = {
            'first_name': 'Test First name',
            'last_name': 'Test Last Name',
            'midl_name': 'Test Midl Name',
            'phone': '+380991234567',
            'email': 'test@mail.com',
            'comment': 'Test comment'
        }
        response = self.client.post(reverse('order:order_create'), data)
        self.assertTrue(data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/success_order.html')

    def test_post_request_valid_data_authenticated_user(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'midl_name': 'Smith',
            'phone': '+380991234567',
            'email': 'john@example.com',
            'comment': 'Test comment'
        }
        self.client.force_login(self.user)
        response = self.client.post(reverse('order:order_create'), data)
        self.assertEqual(response.status_code, 200)
        last_order = Order.objects.last()
        self.assertEqual(last_order.customer, self.user)


class SuccessOrderViewTest(TestCase):
    def test_request(self):
        response = self.client.get(reverse('order:success_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order/success_order.html")
        self.assertIn('cart', response.context)
        self.assertIn('top_categories', response.context)
