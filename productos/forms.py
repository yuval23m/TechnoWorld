from .models import Producto  
from django import forms  
  
  
class Img(forms.ModelForm):  
    class Meta:  
 
        model = Producto  
        #Incluye todos los campos del modelo del producto
        #fields = '__all__'
        #Incluye 1x1 los campos del modelo del producto
        fields = ['nombre','precio','img','marca','tipo']