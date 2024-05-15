from django.urls import path
from .views import UserRegistrationApiView, activate, UserLoginApiView, UserLogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', activate, name='activate'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)