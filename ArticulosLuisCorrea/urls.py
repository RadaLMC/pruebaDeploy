from django.conf.urls import include, url
from .views import listar, nuevo, eliminar, editar

urlpatterns = [
    url(r'^$', listar, name ="listar"),
    url(r'^nuevo/$', nuevo, name = "nuevo"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar, name= "eliminar"),
    url(r'^(?P<pk>[0-9]+)/editar', editar, name= "editar"),
]