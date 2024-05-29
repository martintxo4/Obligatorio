from exceptions.string_invalido import String_invalido
especialidades = [[]]
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

        coso_pum = True
        while coso_pum == True:
            nombre_esp = self.get_especialidad
            precio_esp = self.get_precio
            coso_pum = False    #lo deje asi por si despues usamos lo de los errores aca, despues lo cambiamos si queres, pero es lo mismo
        especialidades.append([nombre_esp,precio_esp])

            

