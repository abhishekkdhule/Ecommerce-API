from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} - {self.id}"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_category")
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.category.name} - {self.name} - {self.id}"
    
class Property(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="property")
    name = models.CharField(max_length=255)
    data_type = models.CharField(choices=[('str', 'String'), ('int', 'Number'), ('choice', 'Choice')], max_length=255)
    regex = models.CharField(max_length=255, null=True, blank=True)
    validations = models.JSONField(null=True, blank=True)
    choices = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.sub_category.category.name} - {self.sub_category.name} - {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.name

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    name = models.CharField(max_length=250, default="base")
    description = models.CharField(max_length=500)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.PositiveIntegerField()
    properties = models.JSONField(default=dict)
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(discount_percent__lte=100), name='discount_lte_100')
        ]

    def __str__(self) -> str:
        return self.product.name + " -- " + self.name
