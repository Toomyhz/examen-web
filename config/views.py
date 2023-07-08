from django.shortcuts import render
from apps.m_tienda.models import Producto

def index(request):
    productos = Producto.objects.order_by('-id')[:3]
    context = {
        'productos':productos
    }
    return render(request, 'pages/index.html', context)