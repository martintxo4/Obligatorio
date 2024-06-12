from entities.socio import Socio
from entities.medico import Medico
from entities.consulta_medica import Consulta_Medica
from entities.especialidad import Especialidad
from exceptions.IntInvalido import IntInvalido
from exceptions.StringInvalido import StringInvalido
from exceptions.CedulaInvalida import CedulaInvalida
from exceptions.TelefonoInvalido import TelefonoInvalido
from exceptions.TipoDeudaInvalida import  TipoSocioInvalida
from exceptions.FechaInvalida import FechaInvalida
from exceptions.EspecialidadNoExiste import EspecialidadNoExiste
from exceptions.MedicoNoExiste import MedicoNoExiste
from exceptions.SocioNoExiste import SocioNoExiste
from exceptions.CantMaxPacientesAlcanzada import CantMaxPacientesAlcanzada
import time


class Policlinica():
    def __init__(self) -> None:
        self.__socios = []
        self.__medicos = []
        self.__especialidades = []
        self.__consultas =[]

    
    
    
    def string_check(string):
        palabras = string.split()
        for i in range(0,len(palabras)):
            if palabras[i].isalpha() != True:
                raise StringInvalido("No es un string válido, ingréselo de nuevo")
        return True
    




    def dar_alta_especialidad(self): #bien
        nombre_especialidad = input("Ingrese el nombre de la especialidad: ")
        precio = int(input("Ingrese el precio asociado: "))
        while True:
            try:
                palabras = nombre_especialidad.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                break
            except StringInvalido: 
                nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
                
        while True:
            try:
                if not isinstance(precio,int):
                    raise IntInvalido
                break
            except IntInvalido:
                precio = int(input("El precio de la especialidad es incorrecto, ingréselo nuevamente. "))

        especialidad = Especialidad(nombre_especialidad,precio)
        self.__especialidades.append(especialidad)




    
   
    def dar_alta_socio(self): #bien
        nombre_socio = input("Ingrese el nombre:")
        while True:
            try:
                palabras = nombre_socio.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                break
            except StringInvalido:
                nombre_socio = input("No es un nombre válido, ingréselo de nuevo")


        apellido_socio = input("Ingrese el apellido:")
        while True:
            try:
                palabras = apellido_socio.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                break
            except StringInvalido:
                apellido_socio = input("No es un nombre válido, ingréselo de nuevo")
        
        cedula_socio = input("Ingrese la cédula de identidad:")
        while True:
            try:
                if not cedula_socio.isdigit():
                    raise CedulaInvalida
                if len(cedula_socio) != 8:
                    raise CedulaInvalida
                break
            except CedulaInvalida:
                cedula_socio = input("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")

            
        fnacimiento_socio = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fnacimiento_socio, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fnacimiento_socio = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

        fingreso_socio = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fingreso_socio, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fingreso_socio = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

        celular_socio= int(input("Ingrese el número de celular:"))
        while True:
            try:
                if len(celular_socio)!=9:
                    raise TelefonoInvalido
                break
            except TelefonoInvalido:
                celular_socio = int(input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX"))

        tipo_socio = input ("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado")
        while True:
            try:
                if tipo_socio != "1" or tipo_socio != "2":
                    raise TipoSocioInvalida
                break
            except TipoSocioInvalida:
                tipo_socio = int(input("El valor ingresado no es correcto, elige la opción 1 o 2"))

        socio = Socio(nombre_socio,apellido_socio,cedula_socio,fnacimiento_socio,fingreso_socio,celular_socio,tipo_socio)
        self.__socios.append(socio)
    
    def dar_alta_medico(self): #bien
        nombre_medico = input ("Ingrese el nombre:")
        while True:
            try:
                palabras = nombre_medico.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                break
            except StringInvalido:
                nombre_medico = input("No es un apellido válido, ingréselo de nuevo")

        apellido_medico = input ("Ingrese el apellido:")
        while True:
            try:
                palabras = apellido_medico.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                break
            except StringInvalido:
                apellido_medico = input("No es un apellido válido, ingréselo de nuevo")
        cedula_medico = input ("Ingrese la cédula de identidad:")
        while True:
            try:
                if not cedula_medico.isdigit():
                    raise CedulaInvalida
                if len(cedula_medico) != 8:
                    raise CedulaInvalida
                break
            except CedulaInvalida:
                cedula_medico = input("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        fnacimiento_medico = input ("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fnacimiento_medico, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fnacimiento_medico = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fingreso_medico = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fingreso_medico, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fingreso_medico = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        celular_medico = input ("Ingrese el número de celular:")
        while True:
            try:
                if not celular_medico.isdigit():
                    raise TelefonoInvalido
                if len(celular_medico)!=9:
                    raise TelefonoInvalido
                break
            except TelefonoInvalido:
                celular_medico = int(input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX"))
        especialidad_medico = input ("Ingrese la especialidad:")
        try:
            palabras = especialidad_medico.split()
            for i in range(0,len(palabras)):
                if palabras[i].isalpha() != True:
                    raise StringInvalido
                
            especialidad = self.buscar_especialidad(especialidad_medico)
            if especialidad == None:
                raise EspecialidadNoExiste
        except EspecialidadNoExiste: 
            while True:
                print("Esta especialidad no esta dada de alta")
                print ("1 - Volver a ingresar la especialidad")
                resp_esp = input("2 - Dar de alta esta especialidad")            
                if resp_esp == 1:
                    especialidad_medico = input ("Ingrese la especialidad:")
                    try:
                        palabras = especialidad_medico.split()
                        for i in range(0,len(palabras)):
                            if palabras[i].isalpha() != True:
                                raise StringInvalido
                    except StringInvalido:
                        pass
                elif resp_esp == 2:
                    self.dar_alta_especialidad
        except StringInvalido:
            especialidad_medico = input("El nombre de la especialidad no es un string, ingréselo nuevamente. ")
                    

        medico = Medico(nombre_medico,apellido_medico,cedula_medico,fnacimiento_medico,fingreso_medico,celular_medico,especialidad_medico)
        self.__medicos.append(medico)
    
    
    def dar_alta_consulta(self):

        nombre_especialidad_consulta = input("Ingrese la especialidad")
        while True:
            try:
                if self.string_check(nombre_especialidad_consulta) != True:
                    raise StringInvalido
                especialidad = self.buscar_especialidad(nombre_especialidad_consulta)
                if especialidad == None:
                    raise EspecialidadNoExiste
            except StringInvalido: 
                nombre_especialidad_consulta = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
            except EspecialidadNoExiste:
                print("Esta especialidad no está dada de alta elija una opción: ")
                print("1 - Volver a ingresar la especialidad")
                resp = input("2 - Dar de alta esta especialidad")
                if resp == 1:
                    pass
                elif resp == 2:
                    self.dar_alta_especialidad()
                    break
            
        nombre_medico_consulta = input("Ingrese la especialidad")
        while True:
            try:
                if self.string_check(nombre_medico_consulta) != True:
                    raise StringInvalido
                medico = self.buscar_especialidad(nombre_medico_consulta)
                if medico == None:
                    raise MedicoNoExiste
            except StringInvalido: 
                nombre_medico_consulta = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
                pass
            except MedicoNoExiste:
                print("Este médico no está dado de alta elija una opción: ")
                print("1 - Volver a ingresar el médico")
                resp = input("2 - Dar de alta el médico")
                if resp == 1:
                    pass
                elif resp == 2:
                    self.dar_alta_medico()
                    break
            
        
        fconsulta = input("Ingrese la fecha de consulta")
        while True:
            try:
                if time.strptime(fconsulta, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fconsulta = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        
        
        
        pacientes_max = input("Ingrese la cantidad de pacientes que se atenderán")
        while True:
            try:
                if not pacientes_max.isdigit():
                    raise IntInvalido
                break
            except IntInvalido:
                pacientes_max = int(input("El numero de pacientes máximo es invalido, seleccione una nueva cantidad"))
        
        consulta = Consulta_Medica(nombre_especialidad_consulta,nombre_medico_consulta,fconsulta,pacientes_max)
        self.__consultas.append(consulta)
        



    def emitir_ticket(self):
        especialidad_ticket = input("Ingrese la especialidad ")

        while True:
            try:
                if self.string_check(especialidad_ticket) != True:
                    raise StringInvalido
                especialidad = self.buscar_especialidad(especialidad_ticket)
                if especialidad == None:
                    raise EspecialidadNoExiste
            except StringInvalido: 
                especialidad_ticket = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
            except EspecialidadNoExiste:
                print("Esta especialidad no está dada de alta elija una opción: ")
                print("1 - Volver a ingresar la especialidad")
                resp = input("2 - Dar de alta esta especialidad")
                if resp == 1:
                    pass
                elif resp == 2:
                    self.dar_alta_especialidad()
                    break

        
        consultas_de_especialidad = []
        for consulta in self.__consultas:
            if consulta.especialidad == especialidad_ticket:
                i +=1
                print(i,"- Doctor: ",consulta.medico," Día de la consulta: ",consulta.fecha_consulta)
                consultas_de_especialidad.append(consulta)

        indice = int(input("Seleccione la opción deseada "))

        if indice <= len(consultas_de_especialidad):
            
            cedula_socio = input("Ingrese cédula de identidad del socio ")

            try:
                socio = self.buscar_socio(cedula_socio)
            
                if socio == None:
                    raise SocioNoExiste
                
                medico = consultas_de_especialidad [indice][1]
                fecha = consultas_de_especialidad [indice][2] 

                consulta = self.buscar_consulta(medico,fecha)

                if len(consulta.pacientes) >= consulta.cant_max_pacientes:
                    raise CantMaxPacientesAlcanzada
                

                

                
            except SocioNoExiste:
                while True:
                    print("Este socio no está dada de alta elija una opción: ")
                    print("1 - Volver a ingresar el socio")
                    resp = input("2 - Dar de alta este socio")
                    if resp == 1:
                        pass
                    elif resp == 2:
                        self.dar_alta_socio()
                    break

            except CantMaxPacientesAlcanzada:
                pass
            


            

            




        
        

        
        

        
        pass
    
    
    
    def consultar_medicos(self): #bien
        nombre_especialidad = input("Ingrese la especialidad: ")
        while True:
            try:
                palabras = nombre_especialidad.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                    
                especialidad = self.buscar_especialidad(nombre_especialidad)
                if especialidad != None:
                    raise EspecialidadNoExiste
                break
            except StringInvalido: 
                nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
            except EspecialidadNoExiste:
                while True:
                    print("Esta especialidad no esta dada de alta")
                    print ("1 - Volver a ingresar la especialidad")
                    resp_esp = input("2 - Dar de alta esta especialidad")            
                    if resp_esp == 1:
                        especialidad_medico = input ("Ingrese la especialidad:")
                        try:
                            palabras = especialidad_medico.split()
                            for i in range(0,len(palabras)):
                                if palabras[i].isalpha() != True:
                                    raise StringInvalido
                        except StringInvalido:
                            pass
                    if resp_esp == 2:
                        self.dar_alta_especialidad()
                        break


        medicos_especialidad = []
        for medico in self.__medicos:
            if especialidad == medico.especialidad:
                medicos_especialidad.append(medico)

        print(medicos_especialidad)
        
        if len(medicos_especialidad) == 0:
            print("No hay médicos asociados a esa especialidad.")
        






    
    def consultar_precios(self): #bien
        nombre_especialidad = input("Ingrese su especialidad: ")
        while True:
            try:
                palabras = nombre_especialidad.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise StringInvalido
                    
                especialidad = self.buscar_especialidad(nombre_especialidad)
                if especialidad == None:
                    raise EspecialidadNoExiste
                break
            except StringInvalido: 
                nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
            except EspecialidadNoExiste:
                while True:
                    print("Esta especialidad no esta dada de alta")
                    print ("1 - Volver a ingresar la especialidad")
                    resp_esp = input("2 - Dar de alta esta especialidad")            
                    if resp_esp == 1:
                        especialidad_medico = input ("Ingrese la especialidad:")
                        try:
                            palabras = especialidad_medico.split()
                            for i in range(0,len(palabras)):
                                if palabras[i].isalpha() != True:
                                    raise StringInvalido
                        except StringInvalido:
                            pass
                    if resp_esp == 2:
                        self.dar_alta_especialidad
            
        print("El precio de esta especialidad es: ",especialidad.precio)
        





    def consultar_deudas(self): #horrible
        tabla_duedas = [[0 for i in range(0,2)]]                            

        for socio in self.__socios:
            tabla_duedas.append(socio.dueda)                                        

        tabla_duedas.pop(0)                                                      
            
        tabla_duedas.sort(key=lambda x: x[1], reverse=True)

        print (tabla_duedas)
        

    


    def consultar_cantidad_consultas(self):
        fecha_inicio = input("Ingrese la fecha de inicio: ")
    
        while True:
            try:
                if time.strptime(fecha_inicio, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fecha_inicio = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                
        fecha_final = input("Ingrese la fecha final")

        while True:
            try:
                if time.strptime(fecha_final, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fecha_final = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

        consultas_entre_fechas = []
        for consulta in self.__consultas:
            if consulta.fecha_consulta >= fecha_inicio and consulta.fecha_consulta <= fecha_final:
                consultas_entre_fechas.append(consulta)
        
        print("La cantidad de consultas entre el ",fecha_inicio, "y",fecha_final,"es: ",len(consultas_entre_fechas))

    def consultar_ganancias(self):
        fecha_inicio = input("Ingrese la fecha de inicio: ")
    
        while True:
            try:
                if time.strptime(fecha_inicio, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fecha_inicio = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                
        fecha_final = input("Ingrese la fecha final")

        while True:
            try:
                if time.strptime(fecha_final, '%Y-%m-%d') == False:
                    raise FechaInvalida
                break
            except FechaInvalida:
                fecha_final = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

        


    def buscar_especialidad(self,nombre_especialidad):
        for especialidad in self.__especialidades:
            if nombre_especialidad == especialidad.nombre:
                return especialidad
        return None

    def buscar_medico(self,cedula_medico):
        for medico in self.__medicos:
            if cedula_medico == medico.cedula:
                return medico
        return None
    
    def buscar_socio(self,cedula_socio):
        for socio in self.__socios:
            if cedula_socio == socio.cedula:
                return socio
        return None
    
    def buscar_consulta(self,medico,fecha):
        for consulta in self.__consultas:
            if consulta.medico == medico and consulta.fecha_consulta == fecha:
                return consulta
        return None
    
    


        
