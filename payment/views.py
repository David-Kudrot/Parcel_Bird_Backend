from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from purchase.models import Order
from purchase.serializers import OrderSerializer
from product.models import CartItem

class CheckoutView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user, ordered=False)

        if not cart_items.exists():
            return Response({"detail": "No items in the cart."}, status=status.HTTP_400_BAD_REQUEST)

        total_cost = sum(item.product.price * item.quantity for item in cart_items)

        # Create the order
        order = Order.objects.create(
            user=user,
            total_cost=total_cost,
            status='just_placed'
        )

        # Associate each cart item with the order
        for cart_item in cart_items:
            order.products.add(cart_item)
            cart_item.ordered = True
            cart_item.save()
        order.save()


        # Optionally, clear the user's cart after creating the order
       

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)