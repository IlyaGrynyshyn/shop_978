from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', "created", "status", "paid"]
    list_filter = ['id', "created", "status", "paid", "status"]
    search_fields = ['id', 'last_name', "email", "phone", "customer"]
    inlines = [OrderItemInline]
