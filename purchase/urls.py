from django.urls import path
from .views import *


urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderAPIView.as_view(), name='order-detail'),
    path('orderitems/', OrderItemAPIView.as_view(), name='orderitem-list'),
    path('orderitems/<int:pk>/', OrderItemAPIView.as_view(), name='orderitem-detail'),
]