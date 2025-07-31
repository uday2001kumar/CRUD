from django.contrib import admin
from .models import Category, Products
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'description')
admin.site.register(Category, CategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'category', 'price', 'stock')
admin.site.register(Products, ProductsAdmin)
