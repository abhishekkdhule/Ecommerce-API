from django.urls import path
from product.views import CategorySubCategoryListView, ProductListView, ProductView


app_name = 'product'

urlpatterns = [
    path('api/v1/product/<int:pk>', ProductView.as_view()),
    path('api/v1/product', ProductListView.as_view()),
    path('api/v1/categories', CategorySubCategoryListView.as_view())
]
