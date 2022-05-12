from django.db import models  
from django.forms import fields  
from .models import Producto  
from django import forms  
  
  
class Img(forms.ModelForm):  
    class Meta:  
 
        model = Producto  
        #Incluye todos los campos del modelo del producto
        fields = '__all__'
        