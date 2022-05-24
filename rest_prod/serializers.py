from rest_framework import serializers
from productos.models import Producto

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre','precio','img','marca','tipo']