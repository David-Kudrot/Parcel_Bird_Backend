from .models import *
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Order
        fields='__all__'