class Cedula_Invalida(Exception):
    pass

    def cant_digitos(cedula):
        if len(cedula)!=8:
            raise Cedula_Invalida("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        else:
            return 0

    def type(cedula):
        if isinstance(cedula,int) == False:
            raise Cedula_Invalida("No es una cédula válida, ingrese valores númericos")