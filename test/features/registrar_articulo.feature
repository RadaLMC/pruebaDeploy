Feature: Como empleado/administrador de la tienda departamental
		quiero dar click en el boton con la etiqueta "Nuevo" que se encuentra en la lista de productos
		para poder visualizar el formulario de entrada, los datos que quiero ingresar son numero de serie, nombre, descripcion, precio unitario y stock.

Scenario: Registrar articulo 
		Given Que selecciono el botón “Nuevo” en el la lista de articulos
		When ingreso los datos del articulo
		Then Puedo ver el articulo en la lista de articulos incluye (numero de serie, nombre, descripcion, precio unitario y stock).