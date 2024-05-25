from rest_framework import viewsets
from rest_framework.response import Response
from .models import Restaurant
from .serializers import *
from product.serializers import *
from django.shortcuts import get_object_or_404
from product.models import Product
from rest_framework.decorators import action


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True, methods=['get'], url_path='res')
    def list_products(self, request, pk=None):
        restaurant = self.get_object()
        products = restaurant.products.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data)
