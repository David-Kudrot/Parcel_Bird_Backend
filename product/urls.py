from django.urls import path
from .views import ProductAPIView, CategoryAPIView, CartItemDetailView


urlpatterns = [
    path('product/', ProductAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),
]




