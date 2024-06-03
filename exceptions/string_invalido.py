class String_Invalido(Exception):
    pass

    def nombre_check(string):
        for i in range(0,len(string)):
            if str.isalpha() == False:
                raise String_Invalido
            else:
                return 0
            
    def apellido_check(string):
        for i in range(0,len(string)):
            if str.isalpha() == False:
                raise String_Invalido
            else:
                return 0
            
    def especialidad_check(string):
        for i in range(0,len(string)):
            if str.isalpha() == False:
                raise String_Invalido
            else:
                return 0
           