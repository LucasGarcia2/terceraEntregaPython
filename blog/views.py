from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'blog/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'blog/agregar_producto.html', {'form': form})

def buscar_producto(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        resultados = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'blog/resultados_busqueda.html', {'resultados': resultados})
    return render(request, 'blog/buscar_producto.html')
