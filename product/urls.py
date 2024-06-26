from django.urls import path
from .views import ProductAPIView, CategoryAPIView, CartItemListView, CartItemDetailView, CustomerAddressCreateAPIView




product_list = ProductAPIView.as_view({
    'get': 'list',
    'post': 'create'
})



product_detail = ProductAPIView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
   
})


urlpatterns = [
    path('product/', product_list, name='product-list-create'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('categories/', CategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    path('cart-item/', CartItemListView.as_view(), name='create-list'),  
    # Handles list and create
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'), 
    # Handles detail operations
    path('customeraddresses/create/', CustomerAddressCreateAPIView.as_view(), name='customeraddress-create'),
]




