from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class CustomerReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer_review.objects.all()
    serializer_class = CustomerReviewSerializer

class CustomerReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer_review.objects.all()
    serializer_class = CustomerReviewSerializer

class CustomerHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer_History.objects.all()
    serializer_class = CustomerHistorySerializer

class CustomerHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer_History.objects.all()
    serializer_class = CustomerHistorySerializer
