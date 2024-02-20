from django.contrib import admin
from cart.models import Cart

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer', 'variant', 'quantity']
