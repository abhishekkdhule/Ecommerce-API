from product.models import Product, Category, SubCategory, Variant, Property
from rest_framework import serializers


class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class VariantProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer2(read_only=True)
    class Meta:
        model = Variant
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # sub_category = serializers.StringRelatedField()
    variants = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ["name", "description", "category", "sub_category", "variants"]

class CreateProductSerializer(serializers.ModelSerializer):
    # variants = VariantSerializer(many=True, write_only=True)
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source=Category)  
    # sub_category_id = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all(), source=SubCategory)

    class Meta:
        model = Product
        fields = '__all__'
    
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name', 'data_type', 'regex', 'validations', 'choices']

class SubCategorySerilizer(serializers.ModelSerializer):
    property = PropertySerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ['name', 'property']

class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerilizer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name', 'sub_category']


class DynamicVariantSerializer(serializers.Serializer, metaclass=serializers.SerializerMetaclass):
    pass