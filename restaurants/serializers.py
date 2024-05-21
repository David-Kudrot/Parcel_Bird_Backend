from rest_framework import serializers
from product.models import Category, Product
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'slug', 'products', 'image', 'latitude', 'longitude', 'total_product_count']
        read_only_fields = ['slug', 'total_product_count']

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        restaurant = Restaurant.objects.create(**validated_data)
        for product_data in products_data:
            product = Product.objects.get(id=product_data.id)
            restaurant.products.add(product)
        return restaurant

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products', [])
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        # Clear existing products and add new ones
        instance.products.clear()
        for product_data in products_data:
            product = Product.objects.get(id=product_data.id)
            instance.products.add(product)
        return instance
