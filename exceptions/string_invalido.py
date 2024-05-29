class String_Invalido(Exception):
    pass

    def nombre_check(string):
        for i in range(0,len(string)):
            if str.isalpha() == False:
                raise String_Invalido("No es un nombre válido, ingréselo de nuevo")
            
    def apellido_check(string):
        for i in range(0,len(string)):
            if str.isalpha() == False:
                raise String_Invalido("No es un apellido válido, ingréselo de nuevo")
            
    def especialidad_check(string):
        for i in range(0,len(string)):
            if str.isalpha() == False:
                raise String_Invalido("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
            
           