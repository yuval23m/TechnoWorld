from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path ('', index, name="Inicio"),
    path ('accounts/', include('allauth.urls'), name="Inicio"),
    path ('index2/', contacto, name="Index2"),
    path ('contacto/', contacto, name="Contacto"),
    path ('inicio-sesion/', sesion, name="Inicio-Sesion"),
    path ('registro/', registro, name="Registro"),
    path ('quienes-somos/', quienes, name="Quienes-Somos"),
    path ('version-pro/', version, name="Version-Pro"),
    path ('subir-img/', subir_img_prod, name="Subir-Foto"),
    path ('modificar/<ID>', modificar_pro, name="Modificar"),
    path ('eliminar/<ID>', eliminar_prod, name="Eliminar"),
    path ('listar-producto', listar_producto, name="ListarProducto"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)