from product.models import Product, Category
from product.serializer import ProductSerializer, CategorySerializer, CreateProductSerializer, VariantSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from product import helper

class ProductView(APIView):

    def get_object(self, pk):
        return Product.objects.get(id=pk)

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put():
        pass

    def delete():
        pass


class ProductListView(APIView):
    
    def get(self, request):
        products = Product.objects.filter()
        product_serializer = ProductSerializer(products, many=True)
        return Response(data=product_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        variants = request.data.pop("variants")
        product_serializer = CreateProductSerializer(data=request.data)
       
        if product_serializer.is_valid():
            product = product_serializer.create(validated_data=product_serializer.validated_data)
            updated_variants = [{'product': product.id, **variant} for variant in variants]
            variant_serializer = VariantSerializer(data=updated_variants, many=True)
            if variant_serializer.is_valid():
                variant_serializer.create(validated_data=variant_serializer.validated_data)
                return  Response(status=status.HTTP_201_CREATED)
        # errors = variant_serializer.errors + product_serializer.errors
            return Response(data=variant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
# class ProductListView(generics.CreateAPIView):
#     serializer_class = CreateProductSerializer
#     queryset = Product.objects.all()
    


class CategorySubCategoryListView(APIView):
    def get(self, request,):
        objs = Category.objects.all()
        serializer = CategorySerializer(objs, many=True)     
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilterProducts(APIView):
    def get(self, request):
        data = request.data
        filtered_product = helper(data)
        return Response(data=filtered_product, status=status.HTTP_200_OK)