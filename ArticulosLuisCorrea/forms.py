# coding: utf-8
from django import forms
from ArticulosLuisCorrea.models import Articulo

class ArticuloForm(forms.ModelForm):
	""" Formulario para dar servicio al modelo Articulo"""

	class Meta(object):
		model = Articulo
		fields = ['numero_de_serie', 'nombre', 'descripcion', 'precio_unitario', 'stock']