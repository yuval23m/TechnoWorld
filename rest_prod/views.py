from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from productos.models import Producto
from rest_prod.serializers import ProdSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_prod(request):
    if request.method == 'GET':
        listaprod = Producto.objects.all()
        serializer = ProdSerializer(listaprod, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = ProdSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
