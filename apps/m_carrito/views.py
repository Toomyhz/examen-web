from django.shortcuts import render
from .carrito import Carrito
from apps.m_tienda.models import Juego,TarjetaRegalo
# Create your views here.
def mostrar_carrito(request):
    carrito = Carrito(request)
    contenido = carrito.obtener_carrito()
    context = {
        'carrito':contenido
        }
    return render(request, 'm_carrito/carrito.html',context)