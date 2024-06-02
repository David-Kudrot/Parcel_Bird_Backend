from django.urls import path
from .views import CheckoutView, paymentSuccessful, PaymentViewSet

urlpatterns = [
    path('checkout/', CheckoutView.as_view({'get': 'list', 'post': 'create'}), name='checkout'),
    path('paymentSuccessful/<str:tran_id>/<int:pk>/', paymentSuccessful.as_view({'get': 'list', 'post': 'create'}), name="paymentSuccessful"),
    path('pay/', PaymentViewSet.as_view({'post': 'create'}), name="payment"),

]
