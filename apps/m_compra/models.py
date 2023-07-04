from django.db import models
from apps.m_tienda.models import Producto
from django.contrib.auth.models import User
# Create your models here.
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    monto_total = models.IntegerField()
    def __str__(self):
        return self.usuario.username
    
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    monto_detalle = models.IntegerField()
    def __str__(self):
        return self.juego