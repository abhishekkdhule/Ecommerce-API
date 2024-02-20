from django.contrib import admin
from product.models import Product, Category, SubCategory, Variant, Property



@admin.register(Product, Category, SubCategory, Variant, Property)
class ProductAdmin(admin.ModelAdmin):
    pass