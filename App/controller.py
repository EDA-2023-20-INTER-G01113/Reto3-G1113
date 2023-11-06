"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
csv.field_size_limit(2147483647)
import tracemalloc
import os
from tabulate import tabulate
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control=model.new_data_structs()
    return control
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    pass


# Funciones para la carga de datos


def load_data(control, data_size):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = load(data_size)
    file_name = cf.data_dir  + file
    input_file = csv.DictReader(open(file_name, encoding='utf-8'))
    for temblor in input_file:
        model.add_data_ms(control, temblor)

    tamaño= size(control['lista_temblores'])
    lista= model.get_data_5(control["lista_temblores"],tamaño)
    return control,tamaño,lista


def load(data_size):
    if data_size==1:
        temblor =  'temblores-utf8-small.csv'
    elif data_size==2:
        temblor =  'temblores-utf8-5pct.csv'
    elif data_size==3:
        temblor =  'temblores-utf8-10pct.csv'
    elif data_size==4:
        temblor =  'temblores-utf8-20pct.csv'
    elif data_size==5:
        temblor =   'temblores-utf8-30pct.csv'
    elif data_size==6:
        temblor  =   'temblores-utf8-50pct.csv'
    elif data_size==7:
        temblor =  'temblores-utf8-80pct.csv'
    elif data_size==8:
        temblor =  'temblores-utf8-large.csv'
    return temblor


# Funciones de ordenamiento
def size(mapa):
    return model.data_size(mapa)

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """

    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,anio_inicio,anio_final):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    respuesta,total =model.req_1(control,anio_inicio,anio_final)
    tamanio = size(respuesta)
    if tamanio>6:
        return model.get_data_3(respuesta,tamanio),total
    return respuesta,total


def req_2(control,im,fm):
    """
    Retorna el resultado del requerimiento 2
    """
    resultado,total = model.req_2(control,im,fm) 
    tamano= size(resultado)
    if tamano>6:
        return model.get_data_3(resultado,tamano),total
    return resultado,total
    # TODO: Modificar el requerimiento 2


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    min_sig = float(input("Ingrese la significancia mínima del evento: "))
    max_gap = float(input("Ingrese la distancia azimutal máxima del evento: "))
    results, leng, dates = model.req_4(control, min_sig, max_gap)
    r_size = lt.size(results)
    if r_size>6:
        return model.get_data_3(results,r_size),leng, dates, results
    return results, leng, dates, results

def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    f_year = int(input("Ingrese el año sobre el cual quiere recibir información: "))
    lat = float(input("Ingrese la latitud de referencia: "))
    long = float(input("Ingrese la longitud de referencia: "))
    radius = float(input("Ingrese el radio sobre el cual quiere recibir eventos: "))
    n_events = int(input("Ingrese el número de eventos: ")) 
    results, post_events, pre_events, total_events, total_dates, sig_code, sig_event, radius_events = model.req_6(control, lat, long, radius, n_events, f_year)
    r_size = lt.size(results)
    if r_size>6:
        return model.get_data_3(results,r_size), post_events, pre_events, total_events, total_dates, sig_code, sig_event, radius_events, results, lat, long, radius
    return results, post_events, pre_events, total_events, total_dates, sig_code, sig_event, radius_events, results, lat, long, radius

def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req = input(f"Ingrese para qué requerimiento quiere visualizar el mapa\n"
                f'0. Carga de datos\n'
                f'1. Requerimiento 1\n'
                f'2. Requerimiento 2\n'
                f'3. Requerimiento 3\n'
                f'4. Requerimiento 4\n'
                f'5. Requerimiento 5\n'
                f'6. Requerimiento 6\n'
                f'7. Requerimiento 7:\n' )
    if req=='0':
        model.req_8(control, req)
    elif req=='4':
        _, _, _, results_list = req_4(control)
        model.req_8(control, req, results_list)
    elif req=='6':
        _, _, _, _, _, _, _, _, results_list, lat, long, radius = req_6(control)   
        model.req_8(control, req, results_list, lat, long, radius)


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
