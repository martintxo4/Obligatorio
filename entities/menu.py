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
            loop = False
        if respuesta == "2":
            loop = False
        if respuesta == "3":
            loop = False
        if respuesta == "4":
            loop = False
        if respuesta == "5":
            loop = False
        if respuesta == "6":
            loop = False
        if respuesta == "7":
            loop = False
        else:
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")

if __name__=="__main__":
    menu()            
            