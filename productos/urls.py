from django.urls import path
from .views import index, contacto, registro, sesion, quienes, version

urlpatterns = [
    path ('', index, name="Inicio"),
    path ('index2/', contacto, name="Index2"),
    path ('contacto/', contacto, name="Contacto"),
    path ('inicio-sesion/', sesion, name="Inicio-Sesion"),
    path ('registro/', registro, name="Registro"),
    path ('quienes-somos/', quienes, name="Quienes-Somos"),
    path ('version-pro/', version, name="Version-Pro"),
    


    
]
