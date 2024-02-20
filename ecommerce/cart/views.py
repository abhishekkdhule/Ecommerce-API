from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from cart.serializer import CartModificationSerializer, CartSerializer
from cart.models import Cart
from rest_framework.response import Response
from rest_framework import status
from users.models import Customer

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_cart(self, customer_id):
        cart_objs = Cart.objects.filter(customer=customer_id)
        return cart_objs
    
    def get(self, request):
        #get user from request and pull their cart, no need of query params
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