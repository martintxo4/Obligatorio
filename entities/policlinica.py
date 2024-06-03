from medico import Medico
from consulta_medica import Consulta_Medica
from especialidad import Especialidad
from especialidad import especialidades
from exceptions.precio_invalido import Precio_Invalido
from exceptions.string_invalido import String_Invalido


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
        Especialidad.alta_especialidad(nombre_especialidad,precio_especialidad)
