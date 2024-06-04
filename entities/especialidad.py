from exceptions.string_invalido import String_Invalido
from exceptions.precio_invalido import Precio_Invalido
especialidades = []
class Especialidad():
    
    def __init__(self,nombre_especialidad, precio):
        self.__nombre_especialidad = nombre_especialidad
        self.__precio = precio
        
    @property
    def get_especialidad(self):
        return self.__nombre_especialidad

    @property
    def get_precio(self):
        return self.__precio


    def alta_especialidad(self):   
        especialidades.append(self)

            

