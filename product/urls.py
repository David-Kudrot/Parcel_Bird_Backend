from django.urls import path
from .views import ProductAPIView, CategoryAPIView, CartItemListView, CartItemDetailView


urlpatterns = [
    path('product/', ProductAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    path('cart-item/', CartItemListView.as_view(), name='create-list'),  
    # Handles list and create
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'), 
    # Handles detail operations
]




