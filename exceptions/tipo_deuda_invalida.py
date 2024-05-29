class Tipo_Deuda_Invalida(Exception):
    pass
    
    def valor_ingresado_incorrecto (tipo_deuda):
        if tipo_deuda != 1 or tipo_deuda !=2:
            raise Tipo_Deuda_Invalida("El valor ingresado no es correcto, elige la opción 1 o 2.")