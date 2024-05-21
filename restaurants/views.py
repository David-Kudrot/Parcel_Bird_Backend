from rest_framework import viewsets
from rest_framework.response import Response
from .models import Restaurant
from .serializers import *
from product.serializers import *
from django.shortcuts import get_object_or_404


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def retrieve(self, request, *args, **kwargs):
        restaurant = self.get_object()
        category_slug = request.query_params.get('category', None)
        
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = restaurant.products.filter(categories=category)
        else:
            products = restaurant.products.all()
        
        serializer = ProductSerializer(products, many=True)
        return Response({
            'id': restaurant.id,
            'name': restaurant.name,
            'slug': restaurant.slug,
            'image': restaurant.image.url if restaurant.image else None,
            'total_product_count': restaurant.total_product_count(),
            'products': serializer.data,
        })
