from django.contrib import admin
from .models import Cliente, TipoProducto, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoProducto)
admin.site.register(Producto)
