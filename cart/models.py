from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

