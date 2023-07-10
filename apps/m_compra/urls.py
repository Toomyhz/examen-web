from django.urls import path
from .views import *
urlpatterns = [
    path("",listar_compras , name='mostrar_compras'),
    path("confirmar/", confirmar_compra, name='confirmar_compra'),
    path("realizar/", realizar_compra, name='realizar_compra'),
    path("detalle/<int:compra_id>/", detalle_compra, name='detalle_compra'),
]