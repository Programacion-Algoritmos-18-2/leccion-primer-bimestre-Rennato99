#clases.py

"""
Creamos la clase padre que se llama Empleado
"""
class Empleado(object): 
	
	# Constructor
	def __init__(self):
		self.nombre = ""
		self.apellido = ""
		self.cedula = ""
		self.comision_fija = 0

	# Métodos set
	def agregar_nombre(self, nombre):
		self.nombre = nombre

	def agregar_apellido(self, apellido):
		self.apellido = apellido

	def agregar_cedula(self, cedula):
		self.cedula = cedula

	def agregar_comision_fija(self, comision_fija):
		self.comision_fija = comision_fija

	# Métodos get
	def obtener_nombre(self):
		return self.nombre

	def obtener_apellido(self):
		return self.apellido

	def obtener_cedula(self):
		return self.cedula

	def obtener_comision_fija(self):
		return self.comision_fija

	# Método para presentar los datos
	def presentar_datos(self):
		cadena = ("\n----------\nInformacion de %s %s\n\tCEDULA: %s" % (self.obtener_nombre(), self.apellido, self.obtener_cedula()))
		return cadena


"""
Creamos la clase EmpleadoFijo que hereda de Empleado
"""
class EmpleadoFijo(Empleado):

	# Constructor que agrega los atributos de la clase padre y aparte dos más
	def __init__(self):
		super(EmpleadoFijo, self).__init__()
		self.sueldo_fijo = 0
		self.descuento_seguro = 0

	# Métodos set
	def agregar_sueldo_fijo(self, sueldo_fijo):
		self.sueldo_fijo = sueldo_fijo

	def agregar_descuento_seguro(self, descuento_seguro):
		self.descuento_seguro = descuento_seguro

	# Métodos get
	def obtener_sueldo_fijo(self):
		return self.sueldo_fijo

	def obtener_descuento_seguro(self):
		return self.descuento_seguro		

	# Método para calcular el sueldo final
	def calcular_sueldo_final(self):
		valor = (self.obtener_sueldo_fijo()*(100-self.obtener_descuento_seguro())) + self.obtener_comision_fija()
		return valor

	# Método para presentar los datos
	def presentar_datos(self):
		"""
		La siguiente cadena llama une la cadena del método de la clase padre "presentar_datos" con el sueldo_fijo, descuento_seguro y el sueldo_final
		"""
		cadena = ("%s\nEmpleado Fijo\nSueldo fijo: %.2f\nDescuento seguro: %.2f\nSueldo final: %.2f\n----------\n"  % (super(EmpleadoFijo, self).presentar_datos(), self.obtener_sueldo_fijo(), self.obtener_descuento_seguro(), self.calcular_sueldo_final()))
		return cadena


"""
Creamos la clase EmpleadoPorHoras que hereda de Empleado
"""
class EmpleadoPorHoras(Empleado):

	# Constructor que agrega los atributos de la clase padre y aparte dos más
	def __init__(self):
		super(EmpleadoPorHoras, self).__init__()
		self.numero_horas = 0
		self.valor_horas = 0

	# Métodos set
	def agregar_numero_horas(self, numero_horas):
		self.numero_horas = numero_horas

	def agregar_valor_horas(self, valor_horas):
		self.valor_horas = valor_horas

	# Metodos get
	def obtener_numero_horas(self):
		return self.numero_horas

	def obtener_valor_horas(self):
		return self.valor_horas

	# Método para calcular el sueldo final
	def calcular_sueldo_final(self):
		valor = self.obtener_numero_horas() * self.obtener_valor_horas() + self.obtener_comision_fija()
		return valor

	# Método para presentar los datos
	def presentar_datos(self):
		"""
		La siguiente cadena llama une la cadena del método de la clase padre "presentar_datos" con el numero_horas, valor_horas y el sueldo_final
		"""
		cadena = ("%s\nEmpleado Por Horas\nNumero horas: %.2f\nValor hora: %.2f\nSueldo final: %.2f\n----------\n"  % (super(EmpleadoPorHoras, self).presentar_datos(), self.obtener_numero_horas(), self.obtener_valor_horas(), self.calcular_sueldo_final()))
		return cadena


"""
Creamos la clase EmpleadoPorSemana que hereda de Empleado
"""
class EmpleadoPorSemana(Empleado):
	
	# Constructor que agrega los atributos de la clase padre y aparte dos más
	def __init__(self):
		super(EmpleadoPorSemana, self).__init__()
		self.numero_semanas = 0
		self.valor_semanal = 0

	# Métodos sete
	def agregar_numero_semanas(self, numero_semanas):
		self.numero_semanas = numero_semanas

	def agregar_valor_semanal(self, valor_semanal):
		self.valor_semanal = valor_semanal

	# Métodos get
	def obtener_numero_semanas(self):
		return numero_semanas

	def obtener_valor_semanal(self):
		return valor_semanal

	# Método para calcular el sueldo final
	def calcular_sueldo_final(self):
		valor = self.obtener_numero_semanas() * self.obtener_valor_semanal() + self.obtener_comision_fija()
		return valor

	# Método para presentar los datos
	def presentar_datos(self):
		"""
		La siguiente cadena llama une la cadena del método de la clase padre "presentar_datos" con el numero_semanas, valor_semanal y el sueldo_final
		"""
		cadena = ("%s\nEmpleado Por Semana\nNumero semanas: %.2f\nValor semanal: %.2f\nSueldo final: %.2f\n----------\n"  % (super(EmpleadoPorSemana, self).presentar_datos(), self.obtener_numero_semanas(), self.obtener_valor_semanal(), self.calcular_sueldo_final()))
		return cadena