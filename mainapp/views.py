from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from mainapp.models import Product, TopCategory, Category


class BaseListView(ListView):
    model = Product
    template_name = "mainapp/mainpage.html"
    context_object_name = 'products'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_category'] = TopCategory.objects.all()
        context['categories'] = Category.objects.filter(top_category=None)
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'mainapp/product_list.html'
    slug_url_kwarg = 'category_slug'
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        top_category_slug = self.kwargs.get('top_category_slug')
        product_count = Product.objects.filter(category__slug=self.kwargs['category_slug']).count()
        top_category = TopCategory.objects.all()

        context['top_category'] = top_category
        context['product_list'] = Product.objects.filter(category__slug=self.kwargs['category_slug'])
        context['product_count'] = product_count
        context['top_category_slug'] = top_category_slug
        context['category_slug'] = self.kwargs['category_slug']
        return context

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(category=category)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/product_page.html'
    slug_url_kwarg = 'product_slug'


