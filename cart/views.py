from django.shortcuts import render, redirect
from .models import Carrito, ItemCarrito, Producto
from .forms import CartItemForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'cart/lista_productos.html', {'productos': productos})

def anadir_al_carrito(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        formulario = CartItemForm(request.POST)
        if formulario.is_valid():
            item_carrito = formulario.save(commit=False)
            item_carrito.carrito = carrito
            item_carrito.producto = producto
            item_carrito.save()
            return redirect('cart:lista_productos')
    else:
        formulario = CartItemForm(initial={'producto': producto})

    return render(request, 'cart/anadir_carrito.html', {'formulario': formulario, 'producto': producto})

def ver_carrito(request):
    cart, created = Carrito.objects.get_or_create(usuario=request.user)
    cart_items = ItemCarrito.objects.filter(carrito=cart)
    return render(request, 'cart/ver_carrito.html', {'cart_items': cart_items})


