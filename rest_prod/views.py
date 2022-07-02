from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,renderer_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from productos.models import Producto,CartItem
from rest_prod.serializers import ProdSerializer,CartItemAddSerializer,CartItemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser 

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes([TemplateHTMLRenderer])
def lista_productosID(request, ID):
    queryset2 = Producto.objects.all()
    queryset3 = Producto.objects.filter(idpro = ID)
    if request.method == 'GET':
        serializer = CartItemAddSerializer()
        data = {'serializer': serializer,'productos':queryset3,'mensaje':"Agrege el producto a su carrito"}
        return Response(data,template_name='elcarritosID.html' )
    elif request.method == 'POST':
        serializer = CartItemAddSerializer(data=request.data, context={'request': request,'producto_id':ID})
        if serializer.is_valid():
            serializer.save()
            data = {'serializer': serializer,'productos':queryset2,'mensaje':"Agregado al Carrito Correctamente"}
            return Response(data,template_name='elcarritos.html' )
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST,template_name='elcarritosID.html' )

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes([TemplateHTMLRenderer])
def lista_productos(request):
    queryset2 = Producto.objects.all()
    if request.method == 'GET':
        serializer = CartItemAddSerializer()
        data = {'serializer': serializer,'productos':queryset2,'mensaje':"Bienvenido "+ request.user.username}
        return Response(data, template_name='elcarritos.html')
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes([TemplateHTMLRenderer])
def lista_carro_prod_reduce(request,ID):
    queryset = CartItem.objects.all()
    if request.method == 'GET':
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_producto = cart_item.get(producto_id=ID)
        producto = get_object_or_404(Producto, idpro=target_producto.producto.idpro)
        if target_producto.cantidad == 0:
            data = {'productos':queryset,'mensaje':"No se puede quitar mas productos"}
            return Response(data,template_name='carrito_user.html')

        target_producto.cantidad = target_producto.cantidad - 1
        producto.cantidad = producto.cantidad + 1
        producto.save()
        target_producto.save()
        data = {'productos':queryset,'mensaje':"Un Producto eliminado del carrito"}
        return Response(data,template_name='carrito_user.html')
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes([TemplateHTMLRenderer])
def lista_carro_prod_del(request,ID):
    queryset = CartItem.objects.all()
    if request.method == 'GET':
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_producto = get_object_or_404(cart_item, producto_id=ID)
        producto = get_object_or_404(Producto, idpro=target_producto.producto.idpro)
        producto.cantidad = producto.cantidad + target_producto.cantidad
        producto.save()
        target_producto.delete()
        data = {'productos':queryset,'mensaje':"Carrito Limpiado"}
        return Response(data,template_name='carrito_user.html')
        
    
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes([TemplateHTMLRenderer])
def lista_carro_prod_add(request,ID):
    queryset = CartItem.objects.all()
    if request.method == 'GET':
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_producto = cart_item.get(producto_id=ID)
        producto = get_object_or_404(Producto, idpro=target_producto.producto.idpro)
        if producto.cantidad <= 0:
            data = {'productos':queryset,'mensaje':"El producto que intentas agregar ya esta vendido"}
            return Response(data,template_name='carrito_user.html')

        target_producto.cantidad = target_producto.cantidad + 1
        producto.cantidad = producto.cantidad - 1
        producto.save()
        target_producto.save()
        data = {'productos':queryset,'mensaje':"Un Producto añadido al carrito"}
        return Response(data,template_name='carrito_user.html')




@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def lista_carro(request):
    queryset2 = CartItem.objects.filter(user=request.user)
    if request.method == 'GET':
        serializer = CartItemAddSerializer()
        data = {'serializer': serializer,'productos':queryset2,'mensaje':"Bienvenido "+ request.user.username+ " a tu carrito de compras"}
        return Response(data, template_name='carrito_user.html')
    
@api_view(['GET','POST'])
@permission_classes((IsAdminUser,))
@renderer_classes([JSONRenderer,TemplateHTMLRenderer])
def lista_prod(request):

    queryset = Producto.objects.all()

    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            serializer = ProdSerializer()
            data = {'productos': queryset,'serializer':serializer,'mensaje':"Bienvenido "+ request.user.username}
            
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
@permission_classes((IsAdminUser,))
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
@permission_classes((IsAdminUser,))
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
