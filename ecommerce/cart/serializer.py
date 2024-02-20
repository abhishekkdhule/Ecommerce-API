from cart.models import Cart
from rest_framework import serializers
from product.serializer import VariantProductSerializer

class CartSerializer(serializers.ModelSerializer):
    variant = VariantProductSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['variant', 'quantity']

class CartModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer', 'variant', 'quantity']


    def save(self, **kwargs):

        return super().save(**kwargs)