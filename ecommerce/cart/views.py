from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from cart.serializer import CartModificationSerializer, CartSerializer, WishlistSerializer, WishlistModificationSerializer
from cart.models import Cart, Wishlist
from rest_framework.response import Response
from rest_framework import status
from users.models import Customer

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_cart(self, customer_id):
        cart_objs = Cart.objects.filter(customer=customer_id)
        return cart_objs
    
    def get(self, request):
        user = request.user
        cart_objs = self.get_user_cart(customer_id=user.id)
        serializer = CartSerializer(cart_objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        cart_data = request.data
        operation = cart_data.pop("operation")
        user = request.user
        cart_data['customer'] = user.customer.id
        serializer = CartModificationSerializer(data=cart_data)
        if serializer.is_valid():
            user_cart = Cart.objects.filter(customer_id=user.customer.id, variant=serializer.validated_data.get('variant')).first()
            if operation == 'add':
                if user_cart:
                    user_cart.quantity += 1
                    user_cart.save()
                else:
                    serializer.save()
            elif operation == 'remove':
                if user_cart:
                    if user_cart.quantity == 1:
                        user_cart.delete()
                    else:
                        user_cart.quantity -= 1
                        user_cart.save()
                else:
                    return Response({"error": "Item does not exists in cart"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class WishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_wishlist(self, customer_id):
        user_wishlist = Wishlist.objects.filter(customer=customer_id)
        return user_wishlist
    
    def get(self, request):
        user = request.user
        customer_id = user.customer.id
        user_wishlist = self.get_user_wishlist(customer_id=customer_id)
        serializer = WishlistSerializer(user_wishlist, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        operation = request.data.pop("operation")
        request_data = request.data
        request_data['customer'] = request.user.customer.id
        if operation in ['add', 'remove']:
            serializer = WishlistModificationSerializer(data=request_data)
            if serializer.is_valid():
                if operation == 'add':
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                if operation == 'remove':
                    wishlisted_item = Wishlist.objects.filter(customer=request_data['customer'], product=request_data['product'])
                    wishlisted_item.delete()
                    return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)