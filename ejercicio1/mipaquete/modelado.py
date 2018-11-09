#clases.py

class Empleado():
	
	def __init__(self):

		self.nombre = ""
		self.apellido = ""
		self.cedula = ""
		self.comision_fija = 0

	def agregar_nombre(self, nombre):
		self.nombre = nombre

	def agregar_apellido(self, apellido):
		self.apellido = apellido

	def agregar_cedula(self, cedula):
		self.cedula = cedula

	def agregar_comision_fija(self, comision_fija):
		self.comision_fija = comision_fija

	def obtener_nombre(self):
		return self.nombre

	def obtener_apellido(self):
		return self.apellido

	def obtener_cedula(self):
		return self.cedula

	def obtener_comision_sfija(self):
		return self.comision_fija

	def presentar_datos(self):
		cadena = ("Informacion de %s %s\n\tCEDULA: %s" % (self.obtener_nombre(), self.apellido, self.obtener_cedula()))
		return cadena

"""
class EmpleadoFijo(Empleado):

	def __init__(self, arg):
		super(EmpleadoFijo, self).__init__()
		self.sueldo_fijo = 0
		self.descuento_seguro = 0

	def setSueldoFijo(self, sueldo_fijo):
		self.sueldo_fijo = sueldo_fijo

	def setDescuentoSeguro(self, descuento_seguro):
		self.descuento_seguro = descuento_seguro

	def getSueldoFijo(self):
		return self.sueldo_fijo

	def getDescuentoSeguro(self):
		return self.descuento_seguro		

"""