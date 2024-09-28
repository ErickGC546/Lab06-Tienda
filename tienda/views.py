from django.shortcuts import render
from .models import Categoria, Producto

def index(request):
    categorias = Categoria.objects.all() 
    productos = Producto.objects.all()
    return render(request, 'index.html', {'categorias': categorias, 'product_list': productos})

def producto(request, producto_id):
    categorias = Categoria.objects.all() 
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto.html', {'categorias': categorias, 'producto': producto})

def productos_por_categoria(request, categoria_id):
    categorias = Categoria.objects.all()  # Para el menú lateral
    categoria = Categoria.objects.get(id=categoria_id)  # La categoría seleccionada
    productos = Producto.objects.filter(categoria=categoria)  # Productos de la categoría
    return render(request, 'productos_por_categoria.html', {
        'categorias': categorias,
        'categoria': categoria,
        'productos': productos
    })
