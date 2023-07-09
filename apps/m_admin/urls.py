from django.urls import path

from .views import listar_adm, crear_producto

urlpatterns = [
    path('', listar_adm, name='listar_adm'),
    path('crearp/', crear_producto, name='crear_producto')
]