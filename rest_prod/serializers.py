from rest_framework import serializers
from productos.models import Producto, CartItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.fields import CurrentUserDefault


class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idpro','nombre','precio','img','marca','tipo','cantidad','is_available']
class CartItemSerializer(serializers.ModelSerializer):
    """
    serializer for cartitem that serialize all fields in 'CartItem' class
    model and add 'product' as relation
    """

    producto = ProdSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'cantidad', 'producto')
        
class CartItemAddSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ('id','cantidad')
        extra_kwargs = {
            'cantidad': {'required': True},
            'id': {'required': True},
        }
        
    def create(self, validated_data):

        user = User.objects.get(id=self.context['request'].user.id)
        producto = get_object_or_404(Producto, idpro=validated_data['id'])
        if producto.cantidad == 0 or producto.is_available is False:
            raise serializers.ValidationsError(
                {'not available': 'the product is not available.'})

        cart_item = CartItem.objects.create(
            producto=producto,
            user=user,
            cantidad=validated_data['cantidad']
            )
        cart_item.save()
        producto.cantidad = producto.cantidad - cart_item.cantidad
        producto.save()
        return cart_item