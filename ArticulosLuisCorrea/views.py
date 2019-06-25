from django.shortcuts import render, redirect, get_object_or_404
from ArticulosLuisCorrea.models import Articulo
from ArticulosLuisCorrea.forms import ArticuloForm

def listar(request):
	articulos = Articulo.objects.all()
	return render(request, 'articulos/lista.html', {'articulos':articulos})

def nuevo(request):
	if request.method == "POST":
		form = ArticuloForm(request.POST)
		print request.POST
		if form.is_valid():
			articulo = form.save()
			articulo.save()
			return redirect('listar')
	else:
		form = ArticuloForm
	return render(request,'articulos/articulo_nuevo.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminar(request, pk):
	articulo = get_object_or_404(Articulo, pk = pk)
	#articulo = articulo.objects.get(pk = pk)
	articulo.delete()
	return redirect('listar')

def editar(request, pk):
	articulo = get_object_or_404(Articulo, pk = pk)
	if request.method == "POST":
		form = ArticuloForm(request.POST, instance = articulo)
		print request.POST
		if form.is_valid():
			articulo = form.save()
			articulo.save()
			return redirect('listar')
	else:
		form = ArticuloForm (instance=articulo)
	return render(request,'articulos/articulo_nuevo.html',{'form':form, 'etiqueta':'Actualizar'})
