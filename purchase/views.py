from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics, status

# Create your views here.
class OrderAPIView(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        # Retrieve a single product instance
        if pk:
            order = self.get_object(pk)
            serializer = self.serializer_class(order)
            return Response(serializer.data)
        else:
            # Retrieve all products
            order = self.queryset.all()
            serializer = self.serializer_class(order, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        # Create a new product
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
        

