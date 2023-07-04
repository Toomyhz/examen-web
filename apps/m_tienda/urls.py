from django.urls import path

from .views import tienda, filtrar_productos

urlpatterns = [
    path('', tienda, name='tienda'),
    path('filtrar_productos/', filtrar_productos, name='filtrar_productos'),
]
