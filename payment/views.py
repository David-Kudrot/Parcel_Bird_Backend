from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from purchase.models import Order
from purchase.serializers import OrderSerializer
from product.models import CartItem
from sslcommerz_lib import SSLCOMMERZ 
from User.models import User

import string, random


def transaction_id(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




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
        order.save()


        # Optionally, clear the user's cart after creating the order
       

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 





class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):   

        user = request.user
        cart_items = CartItem.objects.filter(user=user, ordered=False)

        print(cart_items, "==========")

        if not cart_items.exists():
            return Response({"detail": "No items in the cart."}, status=status.HTTP_400_BAD_REQUEST)

        total_cost = sum(item.product.price * item.quantity for item in cart_items)

        tranction = transaction_id()

        print(total_cost, tranction)


        settings = { 'store_id': 'parce66569259986df', 'store_pass': 'parce66569259986df@ssl', 'issandbox': True }
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = total_cost
        post_body['currency'] = "BDT"
        post_body['tran_id'] = tranction
        post_body['success_url'] = f'http://127.0.0.1:8000/api/payment/paymentSuccessful/{tranction}/{request.user.id}/'
        post_body['fail_url'] = "http://127.0.0.1:8000/api/cart-item/"
        post_body['cancel_url'] = "http://127.0.0.1:8000/api/cart-item/"
        post_body['emi_option'] = 0
        post_body['cus_name'] = request.user.first_name
        post_body['cus_email'] = request.user.email
        post_body['cus_phone'] = "01700000000"
        post_body['cus_add1'] = "customer address"
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"


        response = sslcz.createSession(post_body) # API response
        print(response)
        # Need to redirect user to response['GatewayPageURL']
        if response.get('status') == 'SUCCESS':
            gateway_url = response['GatewayPageURL']
            return Response({'payment_url': gateway_url}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Failed to create payment session'}, status=status.HTTP_400_BAD_REQUEST)




class paymentSuccessful(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user, ordered=False)

    def create(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        transaction_id = self.kwargs['tran_id']
    
        user = User.objects.get(id=pk)
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

        # Associate each cart item with the order and mark as ordered
        for cart_item in cart_items:
            cart_item.ordered = True
            cart_item.save()
            order.products.add(cart_item)

        order.ordered = True
        order.transactionId=transaction_id
        order.save()

        # Serialize the order to send to the frontend
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
