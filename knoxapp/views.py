import json
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from knox.models import AuthToken
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import login,logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes,renderer_classes
from knoxapp.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,reverse
########################
@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAdminUser,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def login_custom(request):

    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            serializer = LoginSerializer()
            data = {'serializer':serializer}
            return Response(data, template_name='login.html')
        
        elif request.method == 'POST':
            serializer = AuthTokenSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                login(request, user)
                token = AuthToken.objects.create(user)[1]
                return Response({'serializer': serializer,"data":token,"mensaje": "Logeado Correctamente"},template_name='login.html')
            else:
                errors = {'serializer': serializer,'mensaje':"Logeado Incorrectamente"}
                return Response(errors, template_name='login.html')
            
    if request.method == 'GET':
        serializer = LoginSerializer()
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token = AuthToken.objects.create(user)[1]
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
########################################################
@api_view(['GET','POST'])
#@permission_classes((IsAdminUser,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def register_custom(request):

    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            serializer = RegisterSerializer()
            data = {'serializer':serializer}
            return Response(data, template_name='formulario.html')
        
        elif request.method == 'POST':
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {'serializer': serializer,'mensaje':"Registrado Correctamente, Inicie Sesión"}
                return Response(data,template_name='formulario.html')
            else:
                errors = {'serializer': serializer,'mensaje':"Registrado Incorrectamente"}
                return Response(errors, template_name='formulario.html')
            
    if request.method == 'GET':
        serializer = RegisterSerializer()
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
#@permission_classes((IsAdminUser,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def logout_custom(request):

    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            try:
                borrar = AuthToken.objects.get(user=request.user)
                borrar.delete()
            except AuthToken.DoesNotExist:
                return redirect('Inicio')
                
            logout(request)
            return redirect('Inicio')
    if request.method == 'GET':
        try:
            borrar = AuthToken.objects.get(user=request.user)
            borrar.delete()
        except AuthToken.DoesNotExist:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
            
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        