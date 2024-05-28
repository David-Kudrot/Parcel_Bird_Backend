from django.urls import path
from .views import UserRegistrationApiView, activate, UserLoginApiView, UserLogoutView, RiderProfileUpdate,CustomerReviewAPIView,CustomerHistoryList, CustomerHistoryDetail

urlpatterns = [
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', activate, name='activate'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', RiderProfileUpdate.as_view(), name='profile-update'),
    path('reviews/', CustomerReviewAPIView.as_view(), name='customer-reviews'),
    path('reviews/<int:pk>', CustomerReviewAPIView.as_view(), name='customer-reviews'),  # check it
    path('customer-history/', CustomerHistoryList.as_view(), name='customer-history-list'),
    path('customer-history/<int:pk>/', CustomerHistoryDetail.as_view(), name='customer-history-detail'),
]
