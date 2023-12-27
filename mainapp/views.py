from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from mainapp.models import Product, TopCategory, Category
from mainapp.services import all_objects, get_popular_products, get_product_in_category, get_filter_objects, get_object


class BaseListView(ListView):
    """
    Responsible for display the main page
    """
    model = Product
    template_name = "mainapp/mainpage.html"
    context_object_name = 'products'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_category'] = all_objects(TopCategory)
        context['popular_products'] = get_popular_products(limit=12)

        return context


class ProductDetailView(DetailView):
    """
    Displays the product page
    """
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/product_page.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        top_category = all_objects(TopCategory)
        context['top_category'] = top_category
        return context


class CategoryListView(ListView):
    """
    Displaying a list of products by category
    """
    model = Category
    template_name = 'mainapp/product_list.html'
    slug_url_kwarg = 'category_slug'
    paginate_by = 24

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        products = get_filter_objects(Product, category=category)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category_slug = self.kwargs.get('category_slug')
        top_category_slug = self.kwargs.get('top_category_slug')
        product_count = get_product_in_category(category_slug).count()
        top_category = all_objects(TopCategory)

        context['top_category'] = top_category
        context['product_count'] = product_count
        context['top_category_title'] = get_object(TopCategory, slug=top_category_slug)
        context['category_title'] = get_object(model=self.model, slug=category_slug)
        return context
