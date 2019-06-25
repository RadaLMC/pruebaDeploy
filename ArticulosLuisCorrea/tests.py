from django.core.urlresolvers import resolve
from django.test import TestCase
from ArticulosLuisCorrea.views import nuevo, listar, eliminar, editar
from django.http import HttpRequest
from ArticulosLuisCorrea.models import Articulo

class MainPageRopa(TestCase):

	def test_root_url_resolves_to_articulos_nuevo_view(self):
		found = resolve('/articulos/nuevo/')
		self.assertEqual(found.func, nuevo)

	def test_articulo_nuevo_returns_correct_html(self):
		request = HttpRequest()
		response = nuevo(request)
		self.assertIn(b'<div>',response.content)
		self.assertIn(b'Articulo</h1>',response.content)
		self.assertIn(b'<input type = "submit" value = "Guardar" />', response.content)
		self.assertTrue(response.content.endswith(b'</div>'))

	def test_root_url_resolves_to_articulos_listar_view(self):
		found = resolve('/articulos/')
		self.assertEqual(found.func, listar)

	def test_root_url_resolves_to_articulos_eliminar_view(self):
		found = resolve('/articuloss/0/eliminar')
		self.assertEqual(found.func, eliminar)

	def test_root_url_resolves_to_articulos_editar_view(self):
		found = resolve('/articulos/1/editar/')
		self.assertEqual(found.func, editar)

	def test_articulo_eliminar_returns_correct_error_message(self):
		articulo=Articulo(numero_de_serie='1010101010',nombre='Horno',descripcion='Para calentar alimentos',precio_unitario=750,stock=20)
		articulo.save()
		articulos = Articulo.objects.all()
		self.assertEqual(articulos[0].articulo,'Luis')
		articulos = Articulo.objects.all()
		self.assertEqual(len(articulo),1)
		articuloDel = Articulo.objects.get(articulo='Luis')
		articuloDel.delete()