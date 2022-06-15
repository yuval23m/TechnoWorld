from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import authenticate

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data
    
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('email','password')
        extra_kwargs = {'password': {'write_only': True,'required':True},
                        'email':{'required':True,'help_text':None}}


    
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password': {'write_only': True,'required':True},
                        'email': {'required':True, 'help_text':None},
                        'username': {'required':True, 'help_text':None}}
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'], validated_data['password'])

        return user
