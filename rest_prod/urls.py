from django.urls import path
from rest_prod.views import lista_prod

urlpatterns = [
    path('lista_prod', lista_prod, name="lista_prod")
]
