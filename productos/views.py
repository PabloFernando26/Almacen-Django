from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Categoria, Producto
from .forms import ProductoForm  # este es el formulario que esa en forms.py 

# muestra todas las categorías
def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/home.html', {'categorias': categorias})

# lista de los productos de una categoría específica
def lista_productos(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'productos/lista_productos.html', {'categoria': categoria, 'productos': productos})

# muestra los detalles de un producto específico
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categoria = producto.categoria
    return render(request, 'productos/detalle_producto.html', {'producto': producto, 'categoria': categoria})

# agregar un nuevo producto a una categoría
def agregar_producto(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.categoria = categoria
            producto.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('lista_productos', categoria_id=categoria.id)
        else:
            messages.error(request, 'Hubo un error al agregar el producto. Por favor, revisa los campos.')
    else:
        form = ProductoForm()

    return render(request, 'productos/agregar_producto.html', {'form': form, 'categoria': categoria})

# Vista para editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categoria = producto.categoria

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('lista_productos', categoria_id=categoria.id)
        else:
            messages.error(request, 'Hubo un error al actualizar el producto. Por favor, revisa los campos.')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto, 'categoria': categoria})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categoria = producto.categoria

    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('lista_productos', categoria_id=categoria.id)
    else:
        return render(request, 'productos/eliminar_producto.html', {'producto': producto, 'categoria': categoria})
