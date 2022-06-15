import json
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,LoginSerializer
from django.contrib.auth import login,logout
from knoxapp.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect

# Register API
class RegisterAPIGET(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'formulario.html'
    
    def get(self, request):

        serializer = RegisterSerializer()
        return Response({'serializer': serializer})
   
# Register API
class RegisterAPIPOST(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mensaje_register.html'
    serializer_class = RegisterSerializer
    def post(self, request, format=None):
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                #"token": AuthToken.objects.create(user)[1],
                "mensaje": "Registrado Correctamente"
                })
            else:
                hola = json.dumps(serializer.errors)
                holax = json.loads(hola)
                return Response({"mensaje": holax})
            
    
        

class LoginAPIGET(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    
    def get(self, request, format=None):

        serializer = LoginSerializer()
        return Response({'serializer': serializer})
    
class LoginAPIPOST(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = LoginSerializer
    template_name = 'mensaje.html'
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token = AuthToken.objects.create(user)[1]
            return Response({"data":token,"mensaje": "Logeado Correctamente"})
        else:
            hola = json.dumps(serializer.errors)
            holax = json.loads(hola)
            return Response({"mensaje": holax})
        
class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mensaje.html'
    
    def get(self, request, format=None):
        try:
            borrar = AuthToken.objects.get(user=request.user)
            borrar.delete()
        except AuthToken.DoesNotExist:
            return redirect('Inicio')
            
        logout(request)
        return redirect('Inicio')
        
        