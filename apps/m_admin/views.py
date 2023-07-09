from django.shortcuts import render, redirect
from .forms import FormularioAdmProduct
from apps.m_tienda.models import Producto

# Create your views here.

def listar_adm(request):
    productos = Producto.objects.all()
    context = {
        'productos':productos
    }
    return render(request, 'pages/m_admin/listar.html', context)