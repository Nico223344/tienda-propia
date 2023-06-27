from django import forms
from .models import *


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password']

class ProductoForm(forms.ModelForm):
    class Meta:
        Model = Producto
        fields = ['precio', 'descripcion']

class CategoriaForm(forms.ModelForm):
    class Meta:
        Model = Categoria
        fields = ['descripcion']

class ClienteForm(forms.ModelForm):
    class Meta:
        Model = Cliente
        fields = ['rut', 'nombre']

class FormaPagoForm(forms.ModelForm):
    class Meta:
        Model = FormaPago
        fields = ['numero_tarjeta', 'descripcion', 'valida', 'nombre_titular']

class BoletaPagoForm(forms.ModelForm):
    class Meta:
        Model = Boleta
        fields = ['FormaPago', 'Cliente', 'descripcion']

class DetalleBoletaPagoForm(forms.ModelForm):
    class Meta:
        Model = DetalleBoleta
        fields = ['Boleta', 'Producto', 'descripcion']


