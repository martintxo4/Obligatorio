from medico import Medico
from socio import Socio
from consulta_medica import Consulta_Medica
from especialidad import Especialidad
from especialidad import especialidades
from exceptions.precio_invalido import Precio_Invalido
from exceptions.string_invalido import String_Invalido
from exceptions.cedula_invalida import Cedula_Invalida
from exceptions.telefono_invalido import Telefono_Invalido
from exceptions.tipo_deuda_invalida import  Tipo_socio_Invalida


class Policlinica():



    def dar_alta_especialidad():
        nombre_especialidad = input("Ingrese el nombre de la especialidad: ")
        precio_especialidad = input("Ingrese el precio asociado: ")

        String_Invalido.especialidad_check(nombre_especialidad)
        while String_Invalido.especialidad_check != 0:
            nombre_especialidad = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
            String_Invalido.especialidad_check(nombre_especialidad)

        Precio_Invalido.check_precio(precio_especialidad)
        while Precio_Invalido.check_precio != 0:
            precio_especialidad = input("El precio de la especialidad es incorrecto, ingréselo nuevamente.")
            Precio_Invalido.check_precio(precio_especialidad)
        especialidad = Especialidad(nombre_especialidad,precio_especialidad)
        Especialidad.alta_especialidad(especialidad)


    def dar_alta_socio():
        nombre_socio = input ("Ingrese el nombre:")
        apellido_socio = input ("Ingrese el apellido:")
        cedula_socio = input ("Ingrese la cédula de identidad:")
        fnacimiento_socio = input ("Ingrese la fecha de nacimiento en formato aaaa-mm-dd:")
        fingreso_socio = input ("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
        celular_socio= input ("Ingrese el número de celular:")
        tipo_socio = input ("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado")

        String_Invalido.nombre_check (nombre_socio)
        while String_Invalido.nombre_check != 0:
            nombre_socio = input("No es un nombre válido,ingréselo de nuevo")
            String_Invalido.nombre_check (nombre_socio)

        String_Invalido.apellido_check (apellido_socio)
        while String_Invalido.apellido_check != 0:
            apellido_socio = input("No es un apellido válido, ingréselo de nuevo")
            String_Invalido.apellido_check (apellido_socio)

        Cedula_Invalida.cant_digitos (cedula_socio)
        while Cedula_Invalida.cant_digitos != 0:
            cedula_socio = input ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
            Cedula_Invalida.cant_digitos (cedula_socio)

            #Fecha_Invalida.fnacimiento_check (fnacimiento_socio)
            #while string_invalido.fnacimiento_check != 0 :                                                       MARTIN MARTIN MARTIN
            #    fnacimiento = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")     ESTO LO DEJE ASI PORQUE EXCEPTION NO ESTA HECHA Y NO TENGO NI LA MAS PUTA IDEA DE COMO HACERLA, GG WP
            #    Fecha_Invalida.fnacimiento_check (fnacimiento_socio)                                             copy-paste para hacer fingreso

        Telefono_Invalido.cant_digitos (celular_socio)
        while Telefono_Invalido.cant_digitos != 0:
            celular_socio= input ("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
            Telefono_Invalido.cant_digitos (celular_socio)

        Tipo_socio_Invalida.valor_ingresado_incorrecto(tipo_socio)
        while Tipo_socio_Invalida.valor_ingresado_incorrecto != 0:
            tipo_socio=input("El valor ingresado no es correcto, elige la opción 1 o 2.")
            Tipo_socio_Invalida.valor_ingresado_incorrecto(tipo_socio)

        Socio.alta_socio(nombre_socio,apellido_socio,cedula_socio,fnacimiento_socio,fingreso_socio,celular_socio,tipo_socio)