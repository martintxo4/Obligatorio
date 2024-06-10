from entities.socio import Socio
from entities.medico import Medico
from entities.socio import socios
from entities.medico import medicos
from entities.consulta_medica import Consulta_Medica
from entities.especialidad import Especialidad
from entities.especialidad import especialidades
from exceptions.precio_invalido import Precio_Invalido
from exceptions.string_invalido import String_Invalido
from exceptions.cedula_invalida import Cedula_Invalida
from exceptions.telefono_invalido import Telefono_Invalido
from exceptions.tipo_deuda_invalida import  Tipo_socio_Invalida
from exceptions.fecha_invalida import Fecha_Invalida
from exceptions.EspecialidadNoExiste import EspecialidadNoExiste
from exceptions.MedicoNoExiste import MedicoNoExiste
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
                raise String_Invalido("No es un string válido, ingréselo de nuevo")
        return True
    




    def dar_alta_especialidad(self): #bien
        nombre_especialidad = input("Ingrese el nombre de la especialidad: ")
        precio = int(input("Ingrese el precio asociado: "))
        while True:
            try:
                palabras = nombre_especialidad.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise String_Invalido
                break
            except String_Invalido: 
                nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
                
        while True:
            try:
                if not isinstance(precio,int):
                    raise Precio_Invalido
                break
            except Precio_Invalido:
                precio = int(input("El precio de la especialidad es incorrecto, ingréselo nuevamente. "))

        especialidad = Especialidad(nombre_especialidad,precio)
        self.__especialidades.append(especialidad)





    def especialidad_no_dada_de_alta ():  #mal
        while True:
            nombre_especialidad_consulta = input("Ingrese la especialidad")
            String_Invalido.string_check(nombre_especialidad_consulta)
            while String_Invalido.string_check(nombre_especialidad_consulta) != True:
                nombre_especialidad_consulta = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                String_Invalido.string_check(nombre_especialidad_consulta)
            coso_pum = True
            for i in range(0,len(especialidades)):
                if nombre_especialidad_consulta == especialidades[i][0]:
                    coso_pum = False
            while coso_pum == True:
                print("Esta especialidad no está dada de alta elija una opción: ")
                print("1 - Volver a ingresar la especialidad")
                resp = input("2 - Dar de alta esta especialidad")
                if resp == 1:
                    coso_pum = False
                    pass
                elif resp == 2:
                    Policlinica.dar_alta_especialidad()
                    break
                else:
                    pass
            else: 
                break


    
    
   
    def dar_alta_socio(self): #bien
        nombre_socio = input("Ingrese el nombre:")
        while True:
            try:
                palabras = nombre_socio.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise String_Invalido
                break
            except String_Invalido:
                nombre_socio = input("No es un nombre válido, ingréselo de nuevo")


        apellido_socio = input("Ingrese el apellido:")
        while True:
            try:
                palabras = apellido_socio.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise String_Invalido
                break
            except String_Invalido:
                apellido_socio = input("No es un nombre válido, ingréselo de nuevo")
        
        cedula_socio = int(input("Ingrese la cédula de identidad:"))
        while True:
            try:
                if isinstance(cedula_socio,int) == False:
                    raise Cedula_Invalida
                elif len(cedula_socio)!=8:
                    raise Cedula_Invalida
                break
            except Cedula_Invalida:
                cedula_socio = input("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")

            
        fnacimiento_socio = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fnacimiento_socio, '%Y-%m-%d') == False:
                    raise Fecha_Invalida
                break
            except Fecha_Invalida:
                fnacimiento_socio = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

        fingreso_socio = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fingreso_socio, '%Y-%m-%d') == False:
                    raise Fecha_Invalida
                break
            except Fecha_Invalida:
                fingreso_socio = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

        celular_socio= int(input("Ingrese el número de celular:"))
        while True:
            try:
                if len(celular_socio)!=9:
                    raise Telefono_Invalido
                break
            except Telefono_Invalido:
                celular_socio = int(input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX"))

        tipo_socio = int(input ("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado"))
        while True:
            try:
                if tipo_socio != 1 or tipo_socio !=2:
                    raise Tipo_socio_Invalida
                break
            except Tipo_socio_Invalida:
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
                        raise String_Invalido
                break
            except String_Invalido:
                nombre_medico = input("No es un apellido válido, ingréselo de nuevo")

        apellido_medico = input ("Ingrese el apellido:")
        while True:
            try:
                palabras = apellido_medico.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise String_Invalido
                break
            except String_Invalido:
                apellido_medico = input("No es un apellido válido, ingréselo de nuevo")
        cedula_medico = input ("Ingrese la cédula de identidad:")
        while True:
            try:
                if isinstance(cedula_medico,int) == False:
                    raise Cedula_Invalida
                elif len(cedula_medico)!=8:
                    raise Cedula_Invalida
                break
            except Cedula_Invalida:
                cedula_medico = input("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        fnacimiento_medico = input ("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fnacimiento_medico, '%Y-%m-%d') == False:
                    raise Fecha_Invalida
                break
            except Fecha_Invalida:
                fnacimiento_medico = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fingreso_medico = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        while True:
            try:
                if time.strptime(fingreso_medico, '%Y-%m-%d') == False:
                    raise Fecha_Invalida
                break
            except Fecha_Invalida:
                fingreso_medico = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        celular_medico = input ("Ingrese el número de celular:")
        while True:
            try:
                if len(celular_medico)!=9:
                    raise Telefono_Invalido
                break
            except Telefono_Invalido:
                celular_medico = int(input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX"))
        especialidad_medico = input ("Ingrese la especialidad:")
        try:
            palabras = especialidad_medico.split()
            for i in range(0,len(palabras)):
                if palabras[i].isalpha() != True:
                    raise String_Invalido
        except String_Invalido: 
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
                                raise String_Invalido
                    except String_Invalido:
                        pass
                if resp_esp == 2:
                    self.dar_alta_especialidad
                    

        medico = Medico(nombre_medico,apellido_medico,cedula_medico,fnacimiento_medico,fingreso_medico,celular_medico,especialidad_medico)
        self.__medicos.append(medico)
    
    
    def dar_alta_consulta(self): #mal

        while True:
            nombre_especialidad_consulta = input("Ingrese la especialidad")
            try:
                if self.string_check(nombre_especialidad_consulta) != True:
                    raise String_Invalido
                especialidad = self.buscar_especialidad(nombre_especialidad_consulta)
                if especialidad == None:
                    raise EspecialidadNoExiste
            except String_Invalido: 
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
            
        
        while True:
            nombre_medico_consulta = input("Ingrese la especialidad")
            try:
                if self.string_check(nombre_medico_consulta) != True:
                    raise String_Invalido
                medico = self.buscar_especialidad(nombre_medico_consulta)
                if medico == None:
                    raise MedicoNoExiste
            except String_Invalido: 
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
            
        fecha_consulta = input("Ingrese la fecha de consulta")
        #Fecha_Invalida.fecha_check (fecha_consulta)
        #while string_invalido.fnacimiento_check != 0 :                                                       MARTIN MARTIN MARTIN
        #    fnacimiento = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")     ESTO LO DEJE ASI PORQUE EXCEPTION NO ESTA HECHA Y NO TENGO NI LA MAS PUTA IDEA DE COMO HACERLA, GG WP
        #    Fecha_Invalida.fnacimiento_check (fnacimiento_socio)
        pacientes_max = input("Ingrese la cantidad de pacientes que se atenderán")
        Precio_Invalido.check_precio(pacientes_max)
        while Precio_Invalido.check_precio != True:
            pacientes_max = ("No es un número válido, vuelva a ingresarlo")
            Precio_Invalido.check_precio(pacientes_max)

        consulta = Consulta_Medica(nombre_especialidad_consulta,nombre_medico_consulta,fecha_consulta,pacientes_max)
        Consulta_Medica.alta_consulta(consulta)


    
    
    
    
    def consultar_medicos(self): #bien
        nombre_especialidad = input("Ingrese la especialidad: ")
        while True:
            try:
                palabras = nombre_especialidad.split()
                for i in range(0,len(palabras)):
                    if palabras[i].isalpha() != True:
                        raise String_Invalido
                    
                especialidad = self.buscar_especialidad(nombre_especialidad)
                if especialidad != None:
                    raise EspecialidadNoExiste
                break
            except String_Invalido: 
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
                                    raise String_Invalido
                        except String_Invalido:
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
                        raise String_Invalido
                    
                especialidad = self.buscar_especialidad(nombre_especialidad)
                if especialidad == None:
                    raise EspecialidadNoExiste
                break
            except String_Invalido: 
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
                                    raise String_Invalido
                        except String_Invalido:
                            pass
                    if resp_esp == 2:
                        self.dar_alta_especialidad
            
        print("El precio de esta especialidad es: ",especialidad.precio)
        





    def consultar_deudas(): #horrible
        deudas = []
        socios_deuda = []
        for j in range(0,len(socios)):
            for i in range(0,len(socios)):
                max = 0
                if max < socios[i][7]:
                    max = socios[i][7]
                    deudor = i
                    deudas.append(max)
                    socios_deuda.append(deudor)
        listado_duedas = [socios_deuda,deudas]
        print(listado_duedas)

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
    
    


        
