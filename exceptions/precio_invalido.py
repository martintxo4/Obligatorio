class Precio_Invalido(Exception):
    pass

    def check_precio(precio):
        if isinstance(precio,int) == False:
            raise Precio_Invalido("El precio de la especialidad es incorrecto, ingréselo nuevamente.")

