from django.urls import path

from . import views

urlpatterns = [
    path("", views.mostrar_carrito, name='mostrar_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
]