from django.test import TestCase
from django.urls import reverse
from mainapp.models import Product, Category, TopCategory

class TestBaseListView(TestCase):
    def test_base_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/mainpage.html')
        self.assertTrue('products' in response.context)
        self.assertTrue('top_category' in response.context)
        self.assertTrue('popular_products' in response.context)

class TestProductDetailView(TestCase):
    def setUp(self):
        self.top_category = TopCategory.objects.create(
            title="Test Top Category",
            slug="test-top-category"
        )
        self.category = Category.objects.create(
            top_category=self.top_category,
            title="Test Category",
            slug="test-category"
        )
        self.product = Product.objects.create(
            category=self.category,
            title="Test Product",
            slug="test-product",
            product_code=123346,
            price=10000,
            description="test description",
            qty_product=1,
            ordered=0,
            popular=1
        )
        self.url = reverse('product_detail', kwargs={'product_slug': self.product.slug})

    def test_product_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/product_page.html')
        self.assertTrue('product' in response.context)
        self.assertTrue('top_category' in response.context)

class TestCategoryListView(TestCase):
    def setUp(self):
        self.top_category = TopCategory.objects.create(
            title="Test Top Category",
            slug="test-top-category"
        )
        self.category = Category.objects.create(
            top_category=self.top_category,
            title="Test Category",
            slug="test-category"
        )
        self.url = reverse('category_detail', kwargs={'top_category_slug': self.top_category.slug,'category_slug': self.category.slug})

    def test_category_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/product_list.html')
        self.assertTrue('object_list' in response.context)
        self.assertTrue('top_category' in response.context)
        self.assertTrue('product_count' in response.context)
        self.assertTrue('top_category_title' in response.context)
        self.assertTrue('category_title' in response.context)
