from persona import Persona
from especialidad import get_especialidad 

class Medico (Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular,especialidad):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__especialidad = especialidad

