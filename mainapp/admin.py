from django.contrib import admin

from mainapp.models import Category, Product, TopCategory, ProductImage


class PhotoAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'product_code', 'qty_product', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'product_code')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PhotoAdmin,]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class TopCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'top_category')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TopCategory, TopCategoryAdmin)
