from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,renderer_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from productos.models import Producto
from rest_prod.serializers import ProdSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def lista_prod(request):

    queryset = Producto.objects.all()

    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            serializer = ProdSerializer()
            data = {'productos': queryset,'serializer':serializer}
            
            return Response(data, template_name='home.html')
        elif request.method == 'POST':
            serializer = ProdSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {'productos': queryset,'serializer': serializer,'mensaje':"Agregado Correctamente"}
                return Response(data,template_name='home.html')
            else:
                errors = {'productos': queryset,'serializer': serializer,'mensaje':"Agregado Incorrectamente"}
                return Response(errors, template_name='home.html')
    if request.method == 'GET':
        serializer = ProdSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT'])
@permission_classes((IsAuthenticated,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def detalle_prod(request,ID):

    queryset = Producto.objects.get(idpro=ID)
 
    if request.accepted_renderer.format == 'html':
        
        if request.method == "GET":
            producto = get_object_or_404(Producto, idpro=ID)
            serializer = ProdSerializer(producto)
            data = {'serializer': serializer,'queryset':queryset}
            return Response(data, template_name='modificar.html')

            
        elif request.method == 'POST':
            producto = get_object_or_404(Producto, idpro=ID)
            serializer = ProdSerializer(producto, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                data = {'serializer': serializer,'queryset':queryset,'mensaje':"Modificado Correctamente"}
                return Response(data, template_name='modificar.html')
            else:
                data = {'serializer': serializer,'queryset':queryset,'mensaje':"Modificado Incorrectamente",}
                return Response(data, template_name='modificar.html')
    if request.method == "GET":
        serializer = ProdSerializer(queryset)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProdSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET','DELETE'])
@permission_classes((IsAuthenticated,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def eliminar_prod(request,ID):
    queryset = Producto.objects.all()
    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
                producto = get_object_or_404(Producto, idpro=ID)
                serializer = ProdSerializer()
                producto.delete()
                data = {'serializer': serializer,'productos': queryset,'mensaje':"Eliminado Correctamente"}
                return Response(data,template_name='home.html')
    if request.method == "DELETE":
        producto = get_object_or_404(Producto, idpro=ID)
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)