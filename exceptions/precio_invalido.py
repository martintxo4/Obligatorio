class Precio_Invalido(Exception):

    def check_precio(precio):
        if isinstance(precio,int):
            raise Precio_Invalido
        else:
            return True

