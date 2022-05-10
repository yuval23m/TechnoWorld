from django.shortcuts import render


class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        super().__init__();


# Create your views here.
def index(request):
    contexto={"nombre":"HOLALJHLHLKHLK"}
    return render(request, 'productos/index.html', contexto)

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