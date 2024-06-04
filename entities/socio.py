from persona import Persona

socios = []
class Socio (Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular,tipo_socio,deuda):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, nro_celular)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__nro_celular = nro_celular
        self.__tipo_socio = tipo_socio
        self.__deuda = deuda

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
    def get_tipo (self):
        return self.__tipo_socio
    
    @property
    def get_deuda(self):
        return self.__deuda

    def alta_socio(self):
        socios.append(self)




        