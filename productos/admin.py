from django.contrib import admin
from .models import CartItem, Cliente, TipoProducto, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(CartItem)
