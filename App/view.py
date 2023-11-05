﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    pass


def print_menu():
    print("Bienvenido")
    print("0- Inicializar analizador")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control,data_size):
    """
    Carga los datos
    """
    control,tamaño, lista= controller.load_data(control,data_size)
    #print(control)
    print("Total de temblores "+str(tamaño))
    #TODO: Realizar la carga de datos
    elems = [x for x in lt.iterator(lista)]
    print(f'\n')
    print(f'{tabulate(elems,headers="keys",tablefmt="grid")}')
    print(f'\n')
    print(r'Open \Data\maps\req0.html on your browser to see an interactive map with your results!')


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control,im,fm):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    res,tamano=controller.req_2(control,im,fm)
    print("El total de resultado es de : "+ str(tamano))
    # TODO: Imprimir el resultado del requerimiento 2
    for x in lt.iterator(res):
        lista = []
        for elem in lt.iterator(x['Details']):
            lista.append(elem)
        x['Details']=tabulate(lista,headers="keys",tablefmt="grid")
    elems = [x for x in lt.iterator(res)]
    print(f'\n')
    print(f'{tabulate(elems,headers="keys",tablefmt="grid")}')
    print(f'\n')
    print(r'Open \Data\maps\req2.html on your browser to see an interactive map with your results!')


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    min_sig = float(input("Ingrese la significancia mínima del evento: "))
    max_gap = float(input("Ingrese la distancia azimutal máxima del evento: "))

    results, length, dates = controller.req_4(control, min_sig, max_gap)
    
    elems = [x for x in lt.iterator(results)]

    print(f'Total different dates: {dates}')
    print(f'Total events between dates {length}')
    print(f'\n')
    print(f'{tabulate(elems,headers="keys",tablefmt="grid")}')
    print(f'\n')
    print(r'Open \Data\maps\req4.html on your browser to see an interactive map with your results!')


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    f_year = int(input("Ingrese el año sobre el cual quiere recibir información: "))
    lat = float(input("Ingrese la latitud de referencia: "))
    long = float(input("Ingrese la longitud de referencia: "))
    radius = float(input("Ingrese el radio sobre el cual quiere recibir eventos: "))
    n_events = int(input("Ingrese el número de eventos: ")) 

    """ f_year = 2022
    lat = 4.674
    long = -74.068
    radius = 3000.0
    n_events = 5
 """
    results, post_events, pre_events, total_events, total_dates, code, event, radius_events = controller.req_6(control, lat, long, radius, n_events, f_year)
    elems = [x for x in lt.iterator(results)]

    print(f'Max event code: {code}')
    print(f'Post n events: {post_events}')
    print(f'Pre n events: {pre_events}')
    print(f'\n')
    
    print(f'Number of events within radius: {radius_events}')
    print(f'Total different dates: {total_dates}')
    print(f'Total events between dates: {total_events}')
    print(f'\n')

    print(f'{"-"*5} Max Event {"-"*5}')
    print(f'{tabulate([event],headers="keys",tablefmt="grid")}')
    print(f'\n')

    print(f'{"-"*5} Nearest Events in chronological order{"-"*5}')
    print(f'Most important events related to the max event: {code}')
    print(f'\n')

    print(f'Consult size: {total_events}. Only first and last 3 results are:')
    print(f'{tabulate(elems,headers="keys",tablefmt="grid")}')
    print(f'\n')
    print(f'\n')
    print(r'Open \Data\maps\req6.html on your browser to see an interactive map with your results!')
def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            message = """
Ingrese 1 si quiere cargar una muestra pequeña de los datos. 
Ingrese 2 si quiere cargar el 5 porciento de los datos.
Ingrese 3 si quiere cargar el 10 porciento de los datos.
Ingrese 4 si quiere cargar el 20 porciento de los datos
Ingrese 5 si quiere cargar el 30 porciento de los datos.
Ingrese 6 si quiere cargar el 50 porciento de los datos
Ingrese 7 si quiere cargar el 80 porciento de los datos
Ingrese 8 si quiere cargar TODOS los datos."""
            data = int(input(message))
            print("Cargando información de los archivos ....\n")
            load_data(control,data)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            im= float(input("INICIAL: "))
            fm=float(input("FINAL: "))
            print_req_2(control,im,fm)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
