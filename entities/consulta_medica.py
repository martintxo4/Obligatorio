from socio import Socio
from medico import Medico

class Consulta_Medica():
    def __init__(self,especialidad,medico,fecha_consulta,cant_max_pacientes):
        self.__especialidad_consulta = especialidad
        self.__medico = medico
        self.__fecha_consulta = fecha_consulta
        self.__lista_pacientes = []
        self.__cant_max_pacientes = cant_max_pacientes

    def alta_consulta(self):
        if len(self.__lista_pacientes)< self.__cant_max_pacientes:
            self.__lista_pacientes.append(self.__especialidad_consulta,self.__medico,self.__fecha_consulta)
