from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from productos.models import Producto
from rest_prod.serializers import ProdSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_prod(request):
    if request.method == 'GET':
        listaprod = Producto.objects.all()
        serializer = ProdSerializer(listaprod, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_prod(request,ID):
    try:
        producto = Producto.objects.get(idpro=ID)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProdSerializer(producto)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProdSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)