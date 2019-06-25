from django.db import models

class Articulo(models.Model):
	numero_de_serie = models.CharField(max_length=50)
	nombre = models.CharField(max_length=125)
	descripcion = models.CharField(max_length=125)
	precio_unitario = models.IntegerField(default=0)
	stock = models.IntegerField(default=0)

	def __unicode__(self):
		return self.nombre
