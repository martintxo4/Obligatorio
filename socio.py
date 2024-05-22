from persona import Persona

class Socio (Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular,tipo_socio,deuda):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__tipo_socio = tipo_socio
        self.__deuda = deuda

        