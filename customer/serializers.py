from rest_framework import serializers
from .models import *

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_review
        fields = '__all__'

class CustomerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_History
        fields = '__all__'

# class CustomerHistoryDetailSerializer(serializers.ModelSerializer):
#     customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     product = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     class Meta:
#         model = Customer_History
#         fields = '__all__'