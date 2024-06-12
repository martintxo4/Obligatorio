from entities.persona import Persona

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
    def nombre(self):
        return self.__nombre

    @property
    def apellido (self):
        return self.__apellido
    
    @property
    def cedula (self):
        return self.__cedula
    
    @property
    def fecha_nacimiento (self):
        return self.__fecha_nacimiento

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso

    @property
    def celular(self):
        return self.__nro_celular
    
    @property
    def especialidad (self):
        return self.__especialidad

    
        



