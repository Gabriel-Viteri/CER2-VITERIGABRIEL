from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('anadir_carrito/<int:id_producto>/', views.anadir_al_carrito, name='anadir_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
]
