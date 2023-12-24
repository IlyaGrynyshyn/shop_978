from django.views.generic import ListView

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
    model = Product
    template_name = 'mainapp/product_list.html'
    slug_url_kwarg = 'category_slug'
    paginate_by = 12

