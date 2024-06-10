class PrecioInvalido(Exception):

    def check_precio(precio):
        if not isinstance(precio,int):
            raise PrecioInvalido
        else:
            return True

