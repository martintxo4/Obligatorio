from especialidad import Especialidad
from socio import Socio
from medico import Medico
from policlinica import Policlinica
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
                if coso_pum == True:
                    print("Esta especialidad no está dada de alta elija una opción: ")
                    print("1 - Volver a ingresar la especialidad")
                    resp = input("2 - Dar de alta esta especialidad")
                    if resp == 1:
                        pass
                    elif resp == 2:
                        Policlinica.dar_alta_especialidad()
                        break
                else: 
                    break
                
            while True:
                nombre_medico_consulta = input("Ingrese el nombre del médico")
                thing_pum = True
                for i in range(0,len(Medico.medicos)):
                    if nombre_medico_consulta == Medico.medicos[i][0]:
                        thing_pum = False
            fecha_consulta = input("Ingrese la fecha de consulta")
            pacientes_max = input("Ingrese la cantidad de pacientes que se atenderán")
            loop = True
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
            