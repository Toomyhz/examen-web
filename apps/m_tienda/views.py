from django.shortcuts import render,redirect
from .models import Producto, Genero, Plataforma, Tipo
# Create your views here.
def tienda(request):
    context = {
        'productos': Producto.objects.all(),
        'generos': Genero.objects.all(),
        'plataformas': Plataforma.objects.all(),
        'tipos': Tipo.objects.all(),
    }
    return render(request, 'pages/m_tienda/tienda.html',context)

def filtrar_productos(request):
    if request.method == 'POST':
        print(request.POST)
        tipos_seleccionados = request.POST.getlist('tipo')
        generos_seleccionados = request.POST.getlist('genero[]')
        plataformas_seleccionados = request.POST.getlist('plataforma[]')

        productos_filtrados = Producto.objects.filter(tipo__in=tipos_seleccionados, genero__in=generos_seleccionados, plataforma__in=plataformas_seleccionados)
        context = {
            'productos': productos_filtrados,
            'generos': Genero.objects.all(),
            'plataformas': Plataforma.objects.all(),
            'tipos': Tipo.objects.all(),
            'tipos_seleccionados': tipos_seleccionados,
            'generos_seleccionados': generos_seleccionados,
            'plataformas_seleccionados': plataformas_seleccionados,
        }
        return render(request, 'pages/m_tienda/tienda.html',context)
    else:
        return redirect('tienda')