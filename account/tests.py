from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import CustomerRegistrationForm
from .models import Customer

REGISTRATION_URL = reverse('account:registration')
PROFILE_URL = reverse('account:profile')


class CustomerRegistrationViewTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'phone': '123456789',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.invalid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'phone': '123456789',
            'password1': 'testpassword',
            'password2': 'testpassword123',
        }

    def test_customer_registration_view(self):
        response = self.client.get(REGISTRATION_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/registration.html")

    def test_registration_form_valid(self):
        response = self.client.post(REGISTRATION_URL, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Customer.objects.filter(username='testuser').exists())

    def test_registration_form_invalid(self):
        response = self.client.post(REGISTRATION_URL, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Customer.objects.filter(username='testuser').exists())


class PublicProfileDetailViewTest(TestCase):
    def test_profile_detail_view(self):
        response = self.client.get(PROFILE_URL)
        self.assertEqual(response.status_code, 302)


class PrivateProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password="<PASSWORD>",
            email="<EMAIL>",
            phone="123456789"
        )
        self.client.force_login(self.user)

    def test_profile_detail_view_authenticated(self):
        response = self.client.get(PROFILE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/profile.html")


class LogoutViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password="<PASSWORD>",
            email="<EMAIL>",
            phone="123456789"
        )
        self.client.force_login(self.user)

    def test_logout_view(self):
        response = self.client.get(reverse('account:logout'))
        self.assertEqual(response.status_code, 302)


    def test_logout_redirects_to_home(self):
        response = self.client.get(reverse('account:logout'))
        self.assertRedirects(response, reverse('home'), status_code=302)


from django.test import TestCase
from account.models import Customer

class TestCustomerRegistrationForm(TestCase):
    def setUp(self):
        self.existing_email = 'existing_email@example.com'
        self.existing_phone = '1234567890'
        Customer.objects.create(email=self.existing_email, phone=self.existing_phone)

    def test_clean_email_existing_email(self):
        form_data = {
            'username': 'testuser',
            'email': self.existing_email,
            'first_name': 'Test',
            'phone': '0987654321',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_clean_phone_existing_phone(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'phone': self.existing_phone,
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_clean_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'phone': '0987654321',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword',
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_clean_valid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'phone': '0987654321',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
