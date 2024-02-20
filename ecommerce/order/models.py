from django.db import models
from product.models import Variant
from users.models import Customer

class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, choices=[('SUCCESSFUL','Successful'), ('FAILED', 'Failed')])
    transaction_id = models.CharField(max_length=255)



class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    variant = models.ForeignKey(to=Variant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    