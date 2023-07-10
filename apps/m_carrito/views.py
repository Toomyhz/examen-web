from django.shortcuts import render,redirect
from .carrito import Carrito
from apps.m_tienda.models import Producto
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def mostrar_carrito(request):
    carrito = Carrito(request)
    contenido = carrito.obtener_carrito()
    for p in contenido:
        p['precio'] = int(float(p['precio']))
        p['subtotal'] = p['precio'] * int(p['cantidad'])

    total = carrito.obtener_precio_total()
    carrito.guardar_carrito()
    for p in contenido: 
        print(p)
    context = {
        'carrito':contenido,
        'total':total
        }
    return render(request, 'pages/m_carrito/carrito.html',context)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.agregar(producto=producto)
    return redirect('mostrar_carrito')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect('mostrar_carrito')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect('mostrar_carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('mostrar_carrito')
