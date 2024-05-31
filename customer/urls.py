from django.urls import path
from .views import *

urlpatterns = [
    path('customer_reviews/', CustomerReviewListCreateAPIView.as_view(), name='customer_review_list_create'),
    path('customer_reviews/<int:pk>/', CustomerReviewRetrieveUpdateDestroyAPIView.as_view(), name='customer_review_detail'),
    path('customer_history/', CustomerHistoryListCreateAPIView.as_view(), name='customer_history_list_create'),
    path('customer_history/<int:pk>/', CustomerHistoryRetrieveUpdateDestroyAPIView.as_view(), name='customer_history_detail'),
]