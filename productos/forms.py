from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'imagen']
        
    # Validación 'precio'
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio

    # Validación'cantidad'
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 0:
            raise forms.ValidationError('La cantidad no puede ser negativa.')
        return cantidad
