import datetime

class FechaInvalida(Exception):
    pass
    
    def fecha_consulta_invalida ():
        fecha_consulta = input ("- Ingrese la fecha de consulta en formato aaaa-mm-dd")
        organa = datetime.strptime(fecha_consulta, "%Y-%m-%d")
                                                                                                      #intento de exception
            
        
    