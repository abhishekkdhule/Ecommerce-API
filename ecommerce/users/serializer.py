from rest_framework import serializers
from users.models import User, Customer
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=60, min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'contact_number', 'password', 'confirm_password']

    def validate(self, attr):
        if attr.get('password', None) != attr.get('confirm_password', None):
            raise serializers.ValidationError("passwords are not matching!")
        return attr
    
    def create(self, validated_data):
        kwargs = validated_data.pop("kwargs")
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        customer = Customer.objects.create(user=user)
        return user
    


class SigninSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=60)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        user = authenticate(email=email, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid Credentials")
        if not user.is_active:
            raise AuthenticationFailed("Inactive User")
        tokens = self.get_user_token(user)
        return {
            "email": email,
            **tokens
        }
    
    def get_user_token(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }
        
