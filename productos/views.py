import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto
from .forms import *

class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        super().__init__();


# Create your views here.
# Create your views here.
def subir_img_prod(request):
  
    if request.method == 'POST':
        form = Img(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return HttpResponse('Subido exitosamente')
    else:
        form = Img()
    return render(request, 'productos/subir_img.html', {'form' : form})


def modificar_pro(request, ID):
    producto = Producto.objects.get(idpro=ID)
    
    datos = {
        'form':Img(instance=producto)
    }
    
    if(request.method == 'POST'):
        form = Img(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            datos['mensaje'] = 'Modificado correctamente'
    
    return render(request, 'productos/modificar.html', datos)
  
 
def eliminar_prod(request, ID):
    producto = Producto.objects.get(idpro=ID)
    datos = {
        'form':Img(instance=producto)
    }
    producto.delete()
    
    return redirect(to='ListarProducto')
def listar_producto(request):
    producto = Producto.objects.all()
    datos = {
        'productos':producto,
    }
    return render(request, 'productos/lista_producto.html', datos)
##def success(request):     
  ##  return HttpResponse('Subido exitosamente')

def index(request):
    producto = Producto.objects.all()
    datos = {
        'productos':producto,
    }
    return render(request, 'productos/index.html', datos)

def contacto(request):
    return render(request, 'productos/contacto.html')

def registro(request):
    return render(request, 'productos/registro.html')

def sesion(request):
    return render(request, 'productos/inicio_sesion.html')
def quienes(request):
    return render(request, 'productos/quienes_somos.html')

def version(request):
    return render(request, 'productos/version_pro.html')
def registroapi(request):
    return render(request, 'productos/registroapi.html')
