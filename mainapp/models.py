from django.db import models
from django.urls import reverse



def content_file_name(instance, filename):
    return f"images/{instance.__class__.__name__}/{filename}"


class TopCategory(models.Model):
    """
    The model that is responsible for the general name of the category.
    For example: Phones
    """
    title = models.CharField(max_length=50, verbose_name="Name of the top category")
    slug = models.SlugField(unique=True, db_index=True)
    category_icon = models.ImageField(upload_to=content_file_name, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("top_category_detail", kwargs={'top_category_slug': self.slug})

    class Meta:
        verbose_name = 'Top Category'
        verbose_name_plural = 'Top Categories'


class Category(models.Model):
    """
    Model responsible for subcategories.
    For example: Smartphone Apple.
    """
    top_category = models.ForeignKey(TopCategory, verbose_name='Parent category', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Name of the category")
    slug = models.SlugField(unique=True, db_index=True)
    vendor_code = models.BigIntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'top_category_slug': self.top_category.slug, 'category_slug': self.slug}
        return reverse("category_detail", kwargs=kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """
    Model responsible for products
    """
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(unique=True, db_index=True, max_length=255)
    product_code = models.IntegerField(verbose_name='Product Code')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    qty_product = models.IntegerField(default=0, verbose_name='Quantity of product')
    ordered = models.IntegerField(default=0, verbose_name='Ordered times')
    views = models.IntegerField(default=0, verbose_name='Viewed times')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-id']


class ProductImage(models.Model):
    """
    Model responsible for product images
    """
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=f'images/product/')

    def __str__(self):
        return self.product.title

    class Meta:
        ordering = ['-id']
