class Precio_Invalido(Exception):

    def check_precio(precio):
        if not isinstance(precio,int):
            raise Precio_Invalido
        else:
            return True

