from rest_framework import serializers
from .models import Product, Category, CartItem, CustomerAddress, Order
from restaurants.models import Restaurant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'date', 'categories', 'restaurant','available']






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

       


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ['recipient_name', 'street_address', 'apartment_address', 'city', 'state', 'postal_code', 'phone_number', 'county']
        
    def create(self, validated_data):
    # Get the user from the context if available
        user = self.context.get('user')

        # Check if user is authenticated
        if user and user.is_authenticated:
            validated_data['user'] = user

        # Call the create method of the super class
        return super().create(validated_data)



# product order section???????????????????????????

class OrderSerializer(serializers.ModelSerializer):
    orderitems = CartItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'orderitems', 'paymentId', 'created', 'ordered']

    def create(self, validated_data):
        user = self.context['user']
        orderitems_data = validated_data.pop('orderitems', [])
        order = Order.objects.create(user=user, **validated_data)
        for item_data in orderitems_data:
            order.orderitems.add(CartItem.objects.create(**item_data))
        return order

    def update(self, instance, validated_data):
        orderitems_data = validated_data.pop('orderitems', None)
        user = self.context['user']
        
        instance.paymentId = validated_data.get('paymentId', instance.paymentId)
        instance.ordered = validated_data.get('ordered', instance.ordered)
        instance.user = user
        instance.save()

        if orderitems_data is not None:
            instance.orderitems.clear()
            for item_data in orderitems_data:
                instance.orderitems.add(CartItem.objects.create(**item_data))
        
        return instance