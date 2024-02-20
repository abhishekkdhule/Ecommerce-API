from django.urls import path

from cart.views import CartView, WishlistView

app_name = 'cart'

urlpatterns = [
    path('cart/', CartView().as_view()),
    path('wishlist/', WishlistView().as_view())
]
