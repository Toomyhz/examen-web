from django.shortcuts import render, redirect
from .models import Compra, DetalleCompra
from apps.m_tienda.models import Producto
from apps.m_carrito.carrito import Carrito
from django.contrib.auth.decorators import login_required
from sweetify import success, warning
from django.views.decorators.cache import never_cache
# Create your views here.
@login_required(login_url='login')
@never_cache
def confirmar_compra(request):
    carrito = Carrito(request)
    contenido_carrito=carrito.obtener_carrito()
    if len(contenido_carrito) == 0:
        warning(request, 'No hay productos en el carrito', button='Ok', timer=3000, toast=True, position='top')
        return redirect('mostrar_carrito')
    else:
        total = carrito.obtener_precio_total()
        context = {
            'carrito':contenido_carrito,
            'total':total
        }
        return render(request, 'pages/m_compra/confirmar_compra.html',context)

def realizar_compra(request):
    carrito = Carrito(request)
    contenido_carrito=carrito.obtener_carrito()
    if len(contenido_carrito) == 0:
        warning(request, 'No hay productos en el carrito', button='Ok', timer=3000, toast=True, position='top')
        return redirect('mostrar_carrito')
    
    total = carrito.obtener_precio_total()
    compra = Compra(usuario=request.user, monto_total=total)
    compra.save()
    for p in contenido_carrito:
        producto = Producto.objects.get(id=p['producto_id'])
        detalle = DetalleCompra(compra=compra, producto=producto, cantidad = p['cantidad'],monto_detalle=p['subtotal'])
        detalle.save()

    carrito.limpiar_carrito()
    detalles=DetalleCompra.objects.filter(compra=compra)
    success(request, 'Compra realizada con éxito', button='Ok', timer=3000, toast=True, position='top')
    context = {
        'compra':compra,
        'detalles':detalles
    }
    return render(request, 'pages/m_compra/compra_realizada.html',context)

def listar_compras(request):
    compras = Compra.objects.filter(usuario=request.user)
    compras=compras.order_by('-id')
    context = {
        'compras':compras
    }
    return render(request, 'pages/m_compra/listar_compras.html',context)

def detalle_compra(request,compra_id):
    compra = Compra.objects.get(id=compra_id)
    detalles=DetalleCompra.objects.filter(compra=compra)
    context = {
        'compra':compra,
        'detalles':detalles
    }
    return render(request, 'pages/m_compra/detalle_compra.html',context)