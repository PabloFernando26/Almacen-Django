from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta de inicio
    path('categoria/<int:categoria_id>/', views.lista_productos, name='lista_productos'),  # Lista productos de una categoría
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  # Detalles de un producto apretado
    path('categoria/<int:categoria_id>/producto/agregar/', views.agregar_producto, name='agregar_producto'),  # Agregar producto a una categoría
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),  # Editar producto
    path('producto/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar producto
]
