from rest_framework import serializers
from .models import Product, Category, CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'date', 'categories']






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'slug']





class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'user', 'quantity']

    def create(self, validated_data):
    # Get the user from the context if available
        user = self.context.get('user')

        # Check if user is authenticated
        if user and user.is_authenticated:
            validated_data['user'] = user

        # Call the create method of the super class
        return super().create(validated_data)

       
