from entities.socio import Socio
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


class Policlinica():
    def __init__(self) -> None:
        self.__socios = []
        self.__medicos = []
        self.__especialidades = []
        self.__consultas =[]

    def dar_alta_especialidad(self):
        nombre_especialidad = input("Ingrese el nombre de la especialidad: ")
        precio = int(input("Ingrese el precio asociado: "))


        palabras = nombre_especialidad.split()
        for i in range(0,len(palabras)):
            if palabras[i].isalpha() != True:
                raise String_Invalido

        if not isinstance(precio,int):
            raise Precio_Invalido
        
        while True:
            try:
                especialidad = Especialidad(nombre_especialidad,precio)
                self.__especialidades.append(especialidad)
                break
            except String_Invalido: 
                nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
            except Precio_Invalido:
                precio = int(input("El precio de la especialidad es incorrecto, ingréselo nuevamente. "))

        """nombre_especialidad = input("Ingrese el nombre de la especialidad: ")
        while String_Invalido.string_check(nombre_especialidad) != True:
            nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente. ")
            String_Invalido.string_check(nombre_especialidad)
        
        precio_especialidad = int(input("Ingrese el precio asociado: "))
        while Precio_Invalido.check_precio(precio_especialidad) != True:
            precio_especialidad = int(input("El precio de la especialidad es incorrecto, ingréselo nuevamente. "))
            Precio_Invalido.check_precio(precio_especialidad)
        especialidad = Especialidad(nombre_especialidad,precio_especialidad)
        Especialidad.alta_especialidad(especialidad)"""
        


    def especialidad_no_dada_de_alta ():
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


    
    
   
    def dar_alta_socio():
        nombre_socio = input ("Ingrese el nombre:")
        String_Invalido.string_check(nombre_socio)
        while String_Invalido.string_check(nombre_socio) != True:
            nombre_socio = input("No es un nombre válido,ingréselo de nuevo")
            String_Invalido.string_check (nombre_socio)
        
        apellido_socio = input ("Ingrese el apellido:")
        String_Invalido.string_check (apellido_socio)
        while String_Invalido.string_check(apellido_socio) != True:
            apellido_socio = input("No es un apellido válido, ingréselo de nuevo")
            String_Invalido.string_check (apellido_socio)
        
        cedula_socio = input ("Ingrese la cédula de identidad:")
        Cedula_Invalida.cant_digitos (cedula_socio)
        while Cedula_Invalida.cant_digitos(cedula_socio) != True:
            cedula_socio = input ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
            Cedula_Invalida.cant_digitos (cedula_socio)
       
        fnacimiento_socio = input ("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        
        fingreso_socio = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        
        celular_socio= input ("Ingrese el número de celular:")
        Telefono_Invalido.cant_digitos (celular_socio)
        while Telefono_Invalido.cant_digitos != 0:
            celular_socio= input ("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
            Telefono_Invalido.cant_digitos (celular_socio)

        tipo_socio = input ("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado")
        Tipo_socio_Invalida.valor_ingresado_incorrecto(tipo_socio)
        while Tipo_socio_Invalida.valor_ingresado_incorrecto != True:
            tipo_socio=input("El valor ingresado no es correcto, elige la opción 1 o 2.")
            Tipo_socio_Invalida.valor_ingresado_incorrecto(tipo_socio)


            #Fecha_Invalida.fnacimiento_check (fnacimiento_socio)
            #while string_invalido.fnacimiento_check != 0 :                                                       MARTIN MARTIN MARTIN
            #    fnacimiento = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")     ESTO LO DEJE ASI PORQUE EXCEPTION NO ESTA HECHA Y NO TENGO NI LA MAS PUTA IDEA DE COMO HACERLA, GG WP
            #    Fecha_Invalida.fnacimiento_check (fnacimiento_socio)                                             copy-paste para hacer fingreso

        Socio.alta_socio(nombre_socio,apellido_socio,cedula_socio,fnacimiento_socio,fingreso_socio,celular_socio,tipo_socio)




    
    def dar_alta_medico():
        nombre_medico = input ("Ingrese el nombre:")
        apellido_medico = input ("Ingrese el apellido:")
        cedula_medico = input ("Ingrese la cédula de identidad:")
        fnacimiento_medico = input ("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        fingreso_medico = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        celular_medico = input ("Ingrese el número de celular:")
        especialidad_medico = input ("Ingrese la especialidad:")

        String_Invalido.string_check (nombre_medico)
        while String_Invalido.string_check != True:
            nombre_medico = input("No es un nombre válido,ingréselo de nuevo")
            String_Invalido.string_check (nombre_medico)

        String_Invalido.string_check (apellido_medico)
        while String_Invalido.string_check != True:
            apellido_medico = input("No es un apellido válido, ingréselo de nuevo")
            String_Invalido.string_check (apellido_medico)

        Cedula_Invalida.cant_digitos (cedula_medico)
        while Cedula_Invalida.cant_digitos != True:
            cedula_medico = input ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
            Cedula_Invalida.cant_digitos (cedula_medico)

            #Fecha_Invalida.fnacimiento_check (fnacimiento_socio)
            #while string_invalido.fnacimiento_check != 0 :                                                       MARTIN MARTIN MARTIN
            #    fnacimiento = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")     ESTO LO DEJE ASI PORQUE EXCEPTION NO ESTA HECHA Y NO TENGO NI LA MAS PUTA IDEA DE COMO HACERLA, GG WP
            #    Fecha_Invalida.fnacimiento_check (fnacimiento_socio)                                             copy-paste para hacer fingreso

        Telefono_Invalido.cant_digitos (celular_medico)
        while Telefono_Invalido.cant_digitos != True:
            celular_medico= input ("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
            Telefono_Invalido.cant_digitos (celular_medico)

        while True:    
            String_Invalido.string_check(especialidad_medico)
            while String_Invalido.string_check != True:
                especialidad_medico = input ("La especialidad debe ser un string.")
                String_Invalido.string_check(especialidad_medico)
            Joaco = True
            for i in range (0,len(especialidades)):
                if especialidad_medico == especialidades[i][0]:
                    Joaco = False        
            while Joaco == True:
                print ("Esta especialidad no esta dada de alta")
                print ("1 - volver a ingresar la especialidad")
                answer_esp = input("2 - Dar de alta esta especialidad")            
                if answer_esp == 1:
                    pass
                if answer_esp == 2:
                    Policlinica.dar_alta_especialidad()
                    break
            else:
                break
            

    
    
    
    
    def dar_alta_consulta():
        while True:
            nombre_especialidad_consulta = input("Ingrese la especialidad")
            String_Invalido.string_check(nombre_especialidad_consulta)
            while String_Invalido.string_check != True:
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

                
        while True:
            nombre_medico_consulta = input("Ingrese el nombre del médico")
            coso_pum = True
            for i in range(0,len(medicos)):
                if nombre_medico_consulta == medicos[i][0]:
                    coso_pum = False
            if coso_pum == True:
                print("Este médico no está dado de alta, elija una opción: ")
                print("1 - Volver a ingresar el médico")
                resp = input("2 - Dar de alta el médico")
                if resp == 1:
                    pass
                elif resp == 2:
                    Policlinica.dar_alta_medico()
                    break
                else:
                    pass
            else:
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


    
    
    
    
    def consultar_medicos():
        while True:
                nombre_especialidad_medicos = input("Ingrese la especialidad")
                String_Invalido.string_check(nombre_especialidad_medicos)
                while String_Invalido.string_check != True:
                    nombre_especialidad_medicos = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                    String_Invalido.string_check(nombre_especialidad_medicos)
                chose_pum = True
                for i in range(0,len(especialidades)):
                    if nombre_especialidad_medicos == especialidades[i][0]:
                        chose_pum = False
                if chose_pum == True:
                    print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                    pass
                else: 
                    break

        for i in range(0,len(medicos)):
            if nombre_especialidad_medicos == medicos[i][6]:
                print([i][0],[i][1])
            else:
                print("No hay médicos asociados a esa especialidad.")


    
    
    def consultar_precios():
        while True:
            nombre_especialidad = input("Ingrese la especialidad")
            String_Invalido.string_check(nombre_especialidad)
            while String_Invalido.string_check != True:
                nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                String_Invalido.string_check(nombre_especialidad)
            skywalker = True
            for i in range(0,len(especialidades)):
                if nombre_especialidad == especialidades[i][0]:
                    skywalker = False
            if skywalker == True:
                print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                pass
            else: 
                break
        
        for i in range(0,len(especialidades)):
            if nombre_especialidad == [i][0]:
                print ("el precio es:", [i][1])
            else:
                ("No existe esa especialidad.")

    def consultar_deudas():
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


        
