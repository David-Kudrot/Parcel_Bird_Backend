from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework import status,generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,RiderProfile
from . import serializers
from . serializers import RiderProfileSerializer

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # making a activation token for this user, and this is one time token, we can sent it for mail verification and password reset for the user
            token = default_token_generator.make_token(user)
            # making uid user.pk mane user er primary key, eta force_bytes byte a convert korbe, r urlsafe_base64_encode korbe jeta user er jonno unique hobe
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            confirm_link = f"https://parcel-bird-backend.onrender.com/user/active/{uid}/{token}"
            
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response("Check Email for confirmation", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('register')
    else:
        return redirect('register')

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(email=email, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                # print("login=========", user.id)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            logout(request)
            return Response({'success': "Logged out successfully"})
        else:
            return Response({'error': "User is not logged in"}, status=status.HTTP_400_BAD_REQUEST)
        
# Rider Profile update create get==================
        
class RiderProfileUpdate(APIView):
    def post(self, request, *args, **kwargs):
        # Get the user from the request
        user = request.user

        # Check if a RiderProfile instance already exists for the user
        try:
            rider_profile = RiderProfile.objects.get(user=user)
            serializer = RiderProfileSerializer(rider_profile, data=request.data, context={'user': user})
        except RiderProfile.DoesNotExist:
            serializer = RiderProfileSerializer(data=request.data, context={'user': user})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # Get the user from the request
        user = request.user

        # Try to retrieve the RiderProfile instance for the user
        try:
            rider_profile = RiderProfile.objects.get(user=user)
            serializer = RiderProfileSerializer(rider_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RiderProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        # Get the user from the request
        user = request.user

        # Try to delete the RiderProfile instance for the user
        try:
            rider_profile = RiderProfile.objects.get(user=user)
            rider_profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RiderProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
        
    
