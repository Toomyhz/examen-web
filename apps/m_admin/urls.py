from django.urls import path

from .views import listar_adm

urlpatterns = [
    path('', listar_adm, name='listar_adm')
]