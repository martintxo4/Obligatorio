class StringInvalido(Exception):
    pass

    def string_check(string):
        palabras = string.split()
        for i in range(0,len(palabras)):
            if palabras[i].isalpha() != True:
                raise StringInvalido("No es un string válido, ingréselo de nuevo")
        return True



       
           