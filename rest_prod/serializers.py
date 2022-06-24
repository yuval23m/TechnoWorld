from rest_framework import serializers
from productos.models import Producto

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
<<<<<<< Updated upstream
        fields = ['nombre','precio','img','marca','tipo']
=======
        fields = ['idpro','nombre','precio','img','marca','tipo','cantidad','is_available']
class CartItemSerializer(serializers.ModelSerializer):

    producto = ProdSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'cantidad', 'producto')
        
class CartItemAddSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ('id','cantidad')
        extra_kwargs = {
            'cantidad': {'required': True},
        }
        
    def create(self, validated_data):

        user = User.objects.get(id=self.context['request'].user.id)
        producto = get_object_or_404(Producto, idpro=self.context['producto_id'])
        #cart_4valid = get_object_or_404(CartItem, producto=producto).count()
        #cart_4valid = CartItem.objects.filter(producto=producto).count()
        if producto.cantidad == 0 or producto.is_available is False:
            raise serializers.ValidationsError(
                {'not available': 'El producto no está disponible.'})
        
        cart_item = CartItem.objects.create(
            producto=producto,
            user=user,
            cantidad=validated_data['cantidad']
            )
        cart_item.save()
        producto.cantidad = producto.cantidad - cart_item.cantidad
        producto.save()
        return cart_item
>>>>>>> Stashed changes
