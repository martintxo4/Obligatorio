class String_Invalido(Exception):
    pass

    def string_check(string):
        palabras = string.split()
        for i in range(len(palabras)):
            palabras[i].isalpha()
            if palabras[i].isalpha() != True:
                raise String_Invalido
            else:
                return 0
            
           