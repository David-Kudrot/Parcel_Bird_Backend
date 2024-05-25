from rest_framework import serializers
from product.models import Category, Product
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'slug', 'image', 'latitude', 'longitude']
