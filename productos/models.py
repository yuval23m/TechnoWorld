from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True,verbose_name='ID')
    nombreCliente = models.CharField(max_length=50,verbose_name='Nombre cliente')

    def __str__(self):
        return self.nombreCliente

class TipoProducto(models.Model):
    idTp = models.AutoField(primary_key=True,verbose_name='ID')
    nombreTp = models.CharField(max_length=50,verbose_name='Nombre Tipo')

    def __str__(self):
        return self.nombreTp

class Producto(models.Model):
    idpro = models.AutoField(primary_key=True,verbose_name='ID')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    precio = models.IntegerField(verbose_name='Precio')
    img = models.ImageField(upload_to = 'fotoproducto/', null=True)
    marca = models.CharField(max_length=20,null=True, blank=True, verbose_name='Marca')
    tipo = models.ForeignKey(TipoProducto,null=True, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)

    def __ini__(self):
        return self.idpro
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.producto.nombre
    def subtotal(self):
        resultado = self.producto.precio * self.cantidad
        return resultado