from especialidad import Especialidad
from socio import Socio
from socio import socios
from medico import Medico
from medico import medicos
from policlinica import Policlinica
from consulta_medica import Consulta_Medica
from exceptions.precio_invalido import Precio_Invalido
from exceptions.string_invalido import String_Invalido
from exceptions.cedula_invalida import Cedula_Invalida
from exceptions.fecha_invalida import Fecha_Invalida
from exceptions.telefono_invalido import Telefono_Invalido
from exceptions.tipo_deuda_invalida import Tipo_socio_Invalida


def menu():
    loop = True

    while loop==True:
        print("Seleccione una opción del menú:")
        print("1. Dar de alta una especialidad")
        print("2. Dar de alta un socio")
        print("3. Dar de alta un médico")
        print("4. Dar de alta una consulta médica")
        print("5. Emitir un ticket de consulta")
        print("6. Realizar consultas")
        print("7. Salir del programa")
        respuesta = input()
        if respuesta == "1":
            Policlinica.dar_alta_especialidad()
            loop = True
        
        if respuesta == "2":
            Policlinica.dar_alta_socio()
            loop = True
        
        if respuesta == "3":
            nombre_medico = input ("Ingrese el nombre:")
            apellido_medico = input ("Ingrese el apellido:")
            cedula_medico = input("Ingrese la cédula de identidad:")
            fnacimiento_medico = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
            fingreso_medico = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
            
            loop = True
        if respuesta == "4":
            Policlinica.dar_alta_consulta()
            loop = True
        if respuesta == "5":
            while True:
                nombre_especialidad_consulta = input("Ingrese la especialidad")
                String_Invalido.especialidad_check(nombre_especialidad_consulta)
                while String_Invalido.especialidad_check != 0:
                    nombre_especialidad_consulta = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                    String_Invalido.especialidad_check(nombre_especialidad_consulta)
                coso_pum = True
                for i in range(0,len(Especialidad.especialidades)):
                    if nombre_especialidad_consulta == Especialidad.especialidades[i][0]:
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
                






            loop = True
        if respuesta == "6":
            print("Seleccione una opción:")
            print("1. Obtener todos los médicos asociados a una especialidad específica")
            print("2. Obtener el precio de una consulta de una especialidad en específico.")
            print("3. Listar todos los socios con sus deudas asociadas en orden ascendente.")
            print("4. Realizar consultas respecto a cantidad de consultas entre dos fechas")
            respuesta2 = input("5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.")
            if respuesta2 == 1:
                Policlinica.consultar_medicos()
            if respuesta2 == 2:

                pass
            if respuesta2 == 3:
                Policlinica.consultar_deudas()
                pass
            if respuesta2 == 4:
                pass
            if respuesta2 == 5:
                especialidad_deseada = input("ingrese la especialidad deseada")
                
                pass
            else:
                pass
            loop = True
        if respuesta == "7":
            loop = False
        else:
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")

