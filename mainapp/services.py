from django.db.models import QuerySet

from mainapp.models import Product


def all_objects(model, select_related: str = None, prefetch_related: str = None) -> QuerySet:
    all_objects = model.objects.all()
    if select_related:
        all_objects = all_objects.select_related(select_related)
    if prefetch_related:
        all_objects = all_objects.prefetch_related(prefetch_related)
    return all_objects

def get_object(model, **kwargs):
    return model.objects.get(**kwargs)

def get_filter_objects(model, **kwargs) -> QuerySet:
    return model.objects.filter(**kwargs)


def get_popular_products(limit: int) -> QuerySet:
    return all_objects(Product).order_by('-popular')[:limit]


def get_product_in_category(category_slug: str) -> QuerySet:
    product_count = Product.objects.filter(category__slug=category_slug)
    return product_count