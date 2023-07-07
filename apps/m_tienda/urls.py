from django.urls import path

from .views import tienda, filtrar_productos ,buscar_productos

urlpatterns = [
    path('', tienda, name='tienda'),
    path('tienda_filtrada/', filtrar_productos, name='filtrar_productos'),
    path('buscar/', buscar_productos, name='buscar')
]
