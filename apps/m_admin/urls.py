from django.urls import path

from .views import listar_adm, crear_producto, editar_producto, borrar_producto

urlpatterns = [
    path('', listar_adm, name='listar_adm'),
    path('crearp/', crear_producto, name='crear_producto'),
    path('editarp/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('borrar_producto/<int:producto_id>/', borrar_producto, name='borrar_producto')
]