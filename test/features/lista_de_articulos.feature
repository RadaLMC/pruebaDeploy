Feature: Como empleado/administrador de la tienda departamental
		quiero ver mi lista de productos en la url http://10.2.49.115:8000/inventario/	
		para poder analizar mi stock de productos.

Scenario: Obtener Lista de productos
		Given Que selecciono el menú articulos
		When Oprimo el botón de “articulos”
		Then Puedo ver la lista completa de los articulos.