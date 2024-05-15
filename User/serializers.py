from rest_framework import serializers
from .models import User


#registration for role admin, rider and customer
# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required=True)
#     role = serializers.ChoiceField(choices=User.role_choices)  # Add role field

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password', 'role']

#     def validate(self, data):
#         """
#         Validate password confirmation.
#         """
#         if data.get('password') != data.get('confirm_password'):
#             raise serializers.ValidationError({'error': "Passwords do not match"})
#         return data

#     def create(self, validated_data):
#         """
#         Create and return a new user instance.
#         """
#         validated_data.pop('confirm_password')
#         role = validated_data.pop('role', 'customer')  # Default role to 'customer' if not provided
#         user = User.objects.create_user(role=role, **validated_data)
#         return user



# only role for rider and customer
from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=[choice for choice in User.role_choices if choice[0] != 'admin'])  # Exclude 'admin' role

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password', 'role']

    def validate(self, data):
        """
        Validate password confirmation.
        """
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({'error': "Passwords do not match"})
        return data

    def create(self, validated_data):
        """
        Create and return a new user instance.
        """
        validated_data.pop('confirm_password')
        role = validated_data.pop('role', 'customer')  # Default role to 'customer' if not provided
        user = User.objects.create_user(role=role, **validated_data)
        return user




class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']
