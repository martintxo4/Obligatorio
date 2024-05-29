from socio import Socio
from medico import Medico

class Consulta_Medica():
    def __init__(self,especialidad,medico,fecha_consulta,lista_pacientes,cant_max_pacientes):
        self.__especialidad_consulta = especialidad
        self.__medico = medico
        self.__fecha_consulta = fecha_consulta
        self.__lista_pacientes = lista_pacientes
        self.__cant_max_pacientes = cant_max_pacientes


