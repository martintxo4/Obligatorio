
class Consulta_Medica():
    def __init__(self,especialidad,medico,fecha_consulta,cant_max_pacientes):
        self.__especialidad_consulta = especialidad
        self.__medico = medico
        self.__fecha_consulta = fecha_consulta
        self.__pacientes = []
        self.__cant_max_pacientes = cant_max_pacientes


    @property
    def especialidad_consulta(self):
        return self.__especialidad_consulta
    
    @property
    def medico(self):
        return self.__medico
    
    @property
    def pacientes(self):
        return self.__pacientes
    
    @property
    def cant_max_pacientes(self):
        return self.__cant_max_pacientes

    @property 
    def fecha_consulta(self):
        return self.__fecha_consulta
    
