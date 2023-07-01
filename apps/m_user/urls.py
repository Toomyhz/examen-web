from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registro,name='register'),
    path('login/',entrar,name='login'),
    path('logout/',salir,name='logout'),
]