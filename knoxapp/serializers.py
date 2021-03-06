from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.authtoken.serializers import AuthTokenSerializer
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
                    msg = ('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('email','password')
        extra_kwargs = {'password': {'write_only': True,'required':True},
                        'email':{'required':True,'help_text':None}}


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
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
