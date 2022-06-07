from django.urls import path
from rest_prod.views import lista_prod, detalle_prod
from rest_prod.viewsLogin import login

urlpatterns = [
    path('lista_prod', lista_prod, name="lista_prod"),
    path('detalle_prod/<ID>', detalle_prod, name="detalle_prod"),
    path('login', login, name='login'),
]
