from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True,verbose_name='ID')
    nombreCliente = models.CharField(max_length=50,verbose_name='Nombre cliente')

    def __str__(self):
        return self.nombreCliente

class TipoProducto(models.Model):
    idTp = models.IntegerField(primary_key=True,verbose_name='ID')
    nombreTp = models.CharField(max_length=50,verbose_name='Nombre Tipo')

    def __str__(self):
        return self.nombreTp

class Producto(models.Model):
    nombre = models.CharField(max_length=20,primary_key=True, verbose_name='Nombre')
    precio = models.IntegerField(verbose_name='Precio')
    marca = models.CharField(max_length=20,null=True, blank=True, verbose_name='Marca')
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

