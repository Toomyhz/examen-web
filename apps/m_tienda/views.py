from django.shortcuts import render,redirect
from .models import Producto, Genero, Plataforma, Tipo
from django.db.models import Q
from django.db.models import Count
# Create your views here.
def tienda(request):

    productos = Producto.objects.all()

    tipos = Tipo.objects.all()
    generos = Genero.objects.all()
    plataformas = Plataforma.objects.all()

    for tipo in tipos:
            cantidad = productos.filter(tipo=tipo).count()
            tipo.cantidad = cantidad

    for plataforma in plataformas:
            cantidad = productos.filter(plataforma=plataforma).count()
            plataforma.cantidad = cantidad

    for genero in generos:
            cantidad = productos.filter(genero=genero).count()
            genero.cantidad = cantidad
    
    context = {
        'productos': productos,
        'generos': generos,
        'plataformas': plataformas,
        'tipos': tipos,
    }
    return render(request, 'pages/m_tienda/tienda.html',context)

def filtrar_productos(request):
    if request.method == 'POST':

        if request.POST.get('tipo') == "Juegos":
            tipos_seleccionados = [1]
        elif request.POST.get('tipo') == "Tarjetas":
            tipos_seleccionados = [2]
        else:
            tipos_seleccionados = request.POST.getlist('tipo')
            
        generos_seleccionados = request.POST.getlist('genero')
        plataformas_seleccionados = request.POST.getlist('plataforma')

        tipos_seleccionados = [int(tipo) for tipo in tipos_seleccionados]
        generos_seleccionados = [int(genero) for genero in generos_seleccionados]
        plataformas_seleccionados = [int(plataforma) for plataforma in plataformas_seleccionados]

        productos_filtrados = Producto.objects.all()

        if tipos_seleccionados:
          productos_filtrados = productos_filtrados.filter(tipo__in=tipos_seleccionados).distinct()

        if generos_seleccionados:
            productos_filtrados = productos_filtrados.filter(genero__in=generos_seleccionados).distinct()

        if plataformas_seleccionados:
            productos_filtrados = productos_filtrados.filter(plataforma__in=plataformas_seleccionados).distinct()

        cantidad_productos = productos_filtrados.count()

        mensaje = ""

        if not productos_filtrados:
            mensaje = "No se encontraron productos según los filtros seleccionados."

        if productos_filtrados.count() == Producto.objects.all().count():
            cantidad_productos = ""

        tipos = Tipo.objects.all()
        generos = Genero.objects.all()
        plataformas = Plataforma.objects.all()

        for tipo in tipos:
            cantidad = Producto.objects.filter(tipo=tipo).count()
            tipo.cantidad = cantidad
        generos = Genero.objects.annotate(cantidad=Count('producto', filter=Q(producto__in=productos_filtrados))).all()
        plataformas = Plataforma.objects.annotate(cantidad=Count('producto', filter=Q(producto__in=productos_filtrados))).all()


        context = {
            'productos': productos_filtrados,
            
            'generos': generos,
            'plataformas': plataformas,
            'tipos': tipos,

            'tipos_seleccionados': tipos_seleccionados,
            'generos_seleccionados': generos_seleccionados,
            'plataformas_seleccionados': plataformas_seleccionados,
            
            'cantidad_productos': cantidad_productos,
            'mensaje': mensaje,
        }
        return render(request, 'pages/m_tienda/tienda.html',context)
    else:
        return redirect('tienda')
    
def buscar_productos(request):
    if request.method == 'POST':
        busqueda = request.POST['busqueda']
        tipos_busqueda = Tipo.objects.filter(nombre__icontains=busqueda)
        generos_busqueda = Genero.objects.filter(nombre__icontains=busqueda)
        plataformas_busqueda = Plataforma.objects.filter(nombre__icontains=busqueda)

        productos = Producto.objects.none()

        for tipo in tipos_busqueda:
            productos = productos | Producto.objects.filter(tipo=tipo)

        for genero in generos_busqueda:
            productos = productos | Producto.objects.filter(genero=genero)

        for plataforma in plataformas_busqueda:
            productos = productos | Producto.objects.filter(plataforma=plataforma)

        productos = productos | Producto.objects.filter(nombre__icontains=busqueda)

        cantidad_productos = productos.count()
        mensaje = ""

        if not productos:
            mensaje = "No se encontraron productos según los filtros seleccionados."

        tipos = Tipo.objects.all()
        generos = Genero.objects.all()
        plataformas = Plataforma.objects.all()

        for tipo in tipos:
            cantidad = Producto.objects.filter(tipo=tipo).count()
            tipo.cantidad = cantidad
        generos = Genero.objects.annotate(cantidad=Count('producto', filter=Q(producto__in=productos))).all()
        plataformas = Plataforma.objects.annotate(cantidad=Count('producto', filter=Q(producto__in=productos))).all()

        context = {
            'productos': productos,
            'generos': generos,
            'plataformas': plataformas,
            'tipos': tipos,
            'cantidad_productos': cantidad_productos,
            'mensaje': mensaje,
            'busqueda': busqueda,
        }
        return render(request, 'pages/m_tienda/tienda.html',context)
    else:
        return redirect('tienda')