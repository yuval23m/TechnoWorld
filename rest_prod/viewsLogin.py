from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
def login(request):
    
    v_username = request.POST.get('email')
    v_password = request.POST.get('password')
    try:
        user = User.objects.get(username = v_username)
    except User.DoesNotExist:
        return Response("Usuario Inválido")

    pass_valido = check_password(v_password, user.password)
    if not pass_valido:
        return Response("Password Incorrecta")

    token, created = Token.objects.get_or_create(user = user)
    return Response(token.key)