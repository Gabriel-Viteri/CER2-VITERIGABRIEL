from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')  

def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def catalogo(request):
    titulo = "Catálogo"
    data = {
        "titulo": titulo
    }
    return render(request,'core/catalogo.html', data)

def solicitud(request):
    titulo = "Recicla!"
    data = {
        "titulo": titulo
    }
    return render(request,'core/solicitud.html', data)

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save() 
    else:
        form = UserCreationForm()    
    return render(request,'registration/register.html',{"form":form}) 
@login_required
def carrito(request):
    titulo = "Carrito"
    data = {
        "titulo": titulo
    }
    return render(request, 'core/carrito.html', data)
