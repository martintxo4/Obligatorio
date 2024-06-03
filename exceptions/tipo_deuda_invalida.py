class Tipo_socio_Invalida(Exception):
    pass
    
    def valor_ingresado_incorrecto (tipo_socio):
        if tipo_socio != 1 or tipo_socio !=2:
            raise Tipo_socio_Invalida("El valor ingresado no es correcto, elige la opción 1 o 2.")
        else:
            return 0