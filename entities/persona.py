from abc import ABC
class Persona(ABC):
    def __init__(self,nombre,apellido,cedula,fecha_nacimiento,fecha_ingreso,nro_celular):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__nro_celular = nro_celular


