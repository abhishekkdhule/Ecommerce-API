from cart.models import Cart, Wishlist
from rest_framework import serializers
from product.serializer import VariantProductSerializer, ProductSerializer2, ProductSerializer

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
    
class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = ['product']

class WishlistModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

    def save(self, **kwargs):
        return super().save(**kwargs)
