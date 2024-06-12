
class Consulta_Medica():
    def __init__(self,especialidad,medico,fecha_consulta,cant_max_pacientes):
        self.__especialidad = especialidad
        self.__medico = medico
        self.__fecha_consulta = fecha_consulta
        self.__pacientes = []
        self.__cant_max_pacientes = cant_max_pacientes


    @property
    def especialidad(self):
        return self.__especialidad
    
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
        

    def lista_pacientes(self):
        self.__pacientes = [0 for i in range(self.__cant_max_pacientes)]

    def agregar_paciente(self,paciente):
        self.__pacientes.append(paciente)
    
