class Telefono_Invalido(Exception):
    pass

    def cant_digitos(telefono):
        if len(telefono)!=9:
            raise Telefono_Invalido("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
        else:
            return 0