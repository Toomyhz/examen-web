from django.shortcuts import render, redirect
from .forms import FormularioAdmProduct
from django.contrib.auth.decorators import login_required
from apps.m_tienda.models import Producto

# Create your views here.

def listar_adm(request):
    productos = Producto.objects.all()
    context = {
        'productos':productos
    }
    return render(request, 'pages/m_admin/listar.html', context)


def crear_producto(request):
    if request.method == 'POST':
        formulario = FormularioAdmProduct(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            print('Producto añadido')
            return redirect('crear_producto')
    else:
        formulario = FormularioAdmProduct()
    context = {'form': formulario}
    return render(request, 'pages/m_admin/crearp.html', context)