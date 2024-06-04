
from especialidad import especialidades
from medico import medicos
from policlinica import Policlinica
from exceptions.string_invalido import String_Invalido


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
            Policlinica.dar_alta_medico()
            loop = True
        if respuesta == "4":
            Policlinica.dar_alta_consulta()
            loop = True
        if respuesta == "5":
            while True:
                nombre_especialidad_ticket_consulta = input("Ingrese la especialidad")
                String_Invalido.string_check(nombre_especialidad_ticket_consulta)
                while String_Invalido.string_check != 0:
                    nombre_especialidad_ticket_consulta = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                    String_Invalido.string_check(nombre_especialidad_ticket_consulta)
                chose_pum = True
                for i in range(0,len(especialidades)):
                    if nombre_especialidad_ticket_consulta == especialidades[i][0]:
                        chose_pum = False
                if chose_pum == True:
                    print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                    pass
                else: 
                    break
            for i in range(0,len(medicos)):
                if nombre_especialidad_ticket_consulta == medicos [i][0]:
                    pass

                
                
                






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

