from django.db import models
from product.models import Product, Variant

from users.models import Customer

class Cart(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    variant = models.ForeignKey(to=Variant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # discounted_cost = models.DecimalField(decimal_places=2)
    # applied_coupon = models.ForeignKye(max_length=50) -> store coupon codes in soe table had have associated discount value in it

    
class Wishlist(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)