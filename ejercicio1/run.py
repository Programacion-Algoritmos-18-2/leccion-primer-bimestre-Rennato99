#Importamos el paquete necesario
from mipaquete.modelado import *


# Cread Empleado
e = Empleado()					# Creamos un objeto empleado
e.agregar_nombre("Luis")		# Agregamos valor al atributo nombre
e.agregar_apellido("Benitez")	# Agregamos valor al atributo apellido
e.agregar_cedula("1110001")		# Agregamos valor al atributo cedula
print(e.presentar_datos)		# Presentamos los datos