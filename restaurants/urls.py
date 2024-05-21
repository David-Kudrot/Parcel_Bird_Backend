from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'res', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
