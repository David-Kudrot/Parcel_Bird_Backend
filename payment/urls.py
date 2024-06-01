from django.urls import path
from .views import CheckoutView, paymentSuccessfull, PaymentViewSet

urlpatterns = [
    path('checkout/', CheckoutView.as_view({'get': 'list', 'post': 'create'}), name='checkout'),
    path('paymentSuccessfull/<str:tran_id>/<int:pk>/', paymentSuccessfull.as_view({'get': 'list', 'post': 'create'}), name="paymentSuccessfull"),
    path('pay/', PaymentViewSet.as_view({'post': 'create'}), name="payment"),

]
