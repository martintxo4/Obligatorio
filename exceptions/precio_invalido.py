class Precio_Invalido(Exception):
    correcto = False

    def check_precio(precio):
        if isinstance(precio,int) == False:
            raise Precio_Invalido(input("El precio de la especialidad es incorrecto, ingréselo nuevamente."))
        else:
            return 0

