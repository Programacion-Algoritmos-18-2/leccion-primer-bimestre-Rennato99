#Importamos el paquete necesario
from mipaquete.modelado import *


# Creamos Empleado
empleado = Empleado()					# Creamos un objeto empleado
empleado.agregar_nombre("Luis")			# Agregamos valor al atributo nombre
empleado.agregar_apellido("Benitez")	# Agregamos valor al atributo apellido
empleado.agregar_cedula("1110001")		# Agregamos valor al atributo cedula
print(empleado.presentar_datos())		# Presentamos los datos

# Creamos un empleado fijo
empleado_fijo = EmpleadoFijo()  					# Creamos un objeto empleadoFijo
empleado_fijo.agregar_nombre("Ana")					# Agregamos el nombre Ana
empleado_fijo.agregar_apellido("Diaz")				# Agregamos el apellido Diaz
comision = float(input("Ingrese comision: "))		
empleado_fijo.agregar_comision_fija(comision)		# Agregamos comision
empleado_fijo.agregar_sueldo_fijo(300.2)			# Agregamos un sueldo fijo
empleado_fijo.agregar_descuento_seguro(10)			# Agregamos valor al seguro
print(empleado_fijo.presentar_datos())				# Presentamos los datos

#Creamos un empleado por horas
empleado_por_horas = EmpleadoPorHoras()				# Creamos un objeto empleado por Horas
nombre = input("Ingrese su nombre: ")
empleado_por_horas.agregar_nombre(nombre)			# Agregamos el nombre 
empleado_por_horas.agregar_apellido("Andrade")		# Agregamos el apellido Andrade
empleado_por_horas.agregar_cedula("112233")			# Agregamos valor al atributo cedula
empleado_por_horas.agregar_numero_horas(15)			# Agregamos alor al atributo numero_horas
empleado_por_horas.agregar_valor_horas(20.2)		# Agregamos alor al atributo valor_horass
print(empleado_por_horas.presentar_datos())			# Presentamos los datos

"""
#Creamos un empleado por semana
empleado_por_semana = EmpleadoPorSemana()
empleado_por_semana.agregar_nombre("Gerson")
empleado_por_semana.agregar_apellido("Santos")
empleado_por_semana.agregar_cedula("1105137234")
empleado_por_semana.agregar_comision_fija(1)
empleado_por_semana.agregar_numero_semanas(1)
empleado_por_semana,agregar_valor_semanal(1)
print(empleado_por_semana.presentar_datos())
"""