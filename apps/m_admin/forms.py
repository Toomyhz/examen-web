from django.forms import (
    ModelForm,
    TextInput,
    Textarea,
    ClearableFileInput,
    Select,
    SelectMultiple
)
from apps.m_tienda.models import Producto

#Formulario de administración de productos
class FormularioAdmProduct(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'tipo', 'genero', 'plataforma', 'consola']
        widgets = {
            'nombre': TextInput(
                attrs={'class':'form-control'}
            ),
            'descripcion': Textarea(
                attrs={'class':'form-control', 'rows': 4} 
            ),
            'precio': TextInput(
                attrs={'class':'form-control'}
            ),
            'imagen': ClearableFileInput(
                attrs={'class':'form-control-file'}
            ),
            'tipo': Select(
                attrs={'class':'form-control'}
            ),
            'genero': SelectMultiple(
                attrs={'class':'form-control'}
            ),
            'plataforma': Select(
                attrs={'class':'form-control'}
            ),
            'consola': TextInput(
                attrs={'class':'form-control'}
            )
        }
