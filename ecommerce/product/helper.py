from product.models import Product, Property
from rest_framework import serializers

def generate_property_serializer(product_id:int):
    product = Product.objects.get(id=product_id)
    sub_category = product.sub_category.id
    properties = Property.objects.filter(sub_category=sub_category)
    property_serializer_fields = dict()
    for property in properties:
        data_type = property.data_type
        name = property.name
        if data_type == 'str':
            property_serializer_fields.update({name: serializers.CharField()})
        if data_type == 'int':
            property_serializer_fields.update({name: serializers.IntegerField()})
        if data_type == 'choice':
            choices_list = property.choices.split('|')
            choices_enum = [(choice, choice) for choice in choices_list]
            property_serializer_fields.update({name: serializers.ChoiceField(choices=choices_enum)})
    PropertySerializer = type('PropertySerializer', (serializers.Serializer,), property_serializer_fields)

    return product, PropertySerializer

def generate_product_serializer(product_id:int):
    pass
    #generate property serializer, then generate 


def filter_data(payload):
    category = payload.get("category")
    sub_category = payload.get("sub_category")
    filters = payload.get("filters")

    for filter in filters:
        pass

    filtered_products = Product.objects.filter(category=category, sub_category=category)
    