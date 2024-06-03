from persona import Persona
from especialidad import get_especialidad 

medicos = [[]]
class Medico (Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular,especialidad):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__nro_celular = nro_celular
        self.__especialidad = especialidad
    
    @property
    def get_nombre(self):
        return self.__nombre

    @property
    def get_apellido (self):
        return self.__apellido
    
    @property
    def get_cedula (self):
        return self.__cedula
    
    @property
    def get_fecha_nacimiento (self):
        return self.__fecha_nacimiento

    @property
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    @property
    def get_celular(self):
        return self.__nro_celular
    
    @property
    def get_especialidad (self):
        return self.__especialidad

    
    def alta_medico(self):
        medicos.append [[self.__nombre,self.__apellido,self.__cedula,self.__fecha_nacimiento,self.__fecha_ingreso,self.__nro_celular,self.__especialidad]]
        



