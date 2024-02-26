from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
