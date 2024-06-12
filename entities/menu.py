from policlinica import Policlinica



def menu():
    policlinica = Policlinica()
    
    while True:
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
            policlinica.dar_alta_especialidad()
        elif respuesta == "2":
            policlinica.dar_alta_socio()
        elif respuesta == "3":
            policlinica.dar_alta_medico()
        elif respuesta == "4":
            policlinica.dar_alta_consulta()
        elif respuesta == "5":
            pass
        elif respuesta == "6":
            print("Seleccione una opción:")
            print("1. Obtener todos los médicos asociados a una especialidad específica")
            print("2. Obtener el precio de una consulta de una especialidad en específico.")
            print("3. Listar todos los socios con sus deudas asociadas en orden ascendente.")
            print("4. Realizar consultas respecto a cantidad de consultas entre dos fechas")
            respuesta2 = input("5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.")
            if respuesta2 == "1":
                policlinica.consultar_medicos()
            elif respuesta2 == "2":

                pass
            elif respuesta2 == "3":
                policlinica.consultar_deudas()
                pass
            elif respuesta2 == "4":
                pass
            elif respuesta2 == "5":
                pass
            else:
                pass
        elif respuesta == "7":
            break
        else:
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")

