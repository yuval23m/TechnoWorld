from django.urls import path
from rest_prod.views import lista_productosID,lista_prod, detalle_prod,eliminar_prod,lista_carro,lista_carro_prod_add,lista_carro_prod_del,lista_carro_prod_reduce
#from rest_prod.viewsLogin import login

urlpatterns = [
    path('lista_prod/', lista_prod, name="lista_prod"),
    path('detalle_prod/<ID>', detalle_prod, name="detalle_prod"),
    path('eliminar/<ID>', eliminar_prod, name="eliminar_prod"),
    #path('login', login, name='login'),

    path('lista_carro/', lista_carro, name="lista_carro"),
    #path('lista_productos/', lista_productos, name="lista_productos"),
    path('lista_productosID/<ID>', lista_productosID, name="lista_productosID"),
    path('lista_carro_prod_add/<ID>', lista_carro_prod_add, name="lista_carro_prod_add"),
    path('lista_carro_prod_reduce/<ID>', lista_carro_prod_reduce, name="lista_carro_prod_reduce"),
    path('lista_carro_prod_del/<ID>', lista_carro_prod_del, name="lista_carro_prod_del"),
]
