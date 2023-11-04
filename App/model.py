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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import datetime
from datetime import date
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    control = {}

    control['lista_temblores'] = lt.newList('ARRAY_LIST', compare)
    
    control['temblores_mag'] = om.newMap(omaptype='BST',
                                      cmpfunction=compareDates)
    control['temblores']= om.newMap(omaptype='BST',
                                      cmpfunction=compareDates)
    return control  


# Funciones para agregar informacion al modelo

def add_data_ms(control, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(control['lista_temblores'], data)
    updateDate(control["temblores_mag"],data)
    uptime(control["temblores"],data)

    return control
    #TODO: Crear la función para agregar elementos a una lista
    pass
def updateDate(mapa, data):
    mag = round(float(data['mag']),3)
    entry = om.get(mapa, mag)
    if entry is None:
        datentry = new_data()
        om.put(mapa,mag, datentry)
    else:
        datentry = me.getValue(entry)
    add_data(datentry, data)
    lt.addLast(datentry["By_mag"],data)
    return mapa

def uptime(mapa,data):
    occurreddate = data['time']
    fecha = datetime.datetime.strptime(occurreddate, "%Y-%m-%dT%H:%M:%S.%fZ")
    dates = fecha.strftime('%Y-%m-%dT%H:%M')
    entry = om.get(mapa, dates)
    if entry is None:
        datentry = lt.newList("ARRAY_LIST")
        om.put(mapa, dates, datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry,data)
    return mapa
# Funciones para creacion de datos

def new_data():
    """ 
    Crea una nueva estructura para modelar los datos
    """
    data= {}
    data["By_depth"]=om.newMap(omaptype='BST',
                                      cmpfunction=compareDates)
    data["By_mag"]= lt.newList("ARRAY_LIST")
    return data

def add_data(structs,data):
    mapa= structs["By_depth"]
    entry= om.get(mapa,data["depth"])
    if entry:
        lista= me.getValue(entry)
    else:
        lista= lt.newList("ARRAY_LIST")
        om.put(mapa,data["depth"],lista)
    lt.addLast(lista,data)
    return structs
#def add_data_by_date(structs,data):
    mapa= structs["By_date"]
    occurreddate = data['time']
    fecha = datetime.datetime.strptime(occurreddate, "%Y-%m-%dT%H:%M:%S.%fZ")
    dates = fecha.strftime('%Y-%m-%dT%H:%M')
    entry = om.get(mapa, dates)
    if entry is None:
        datentry = lt.newList("ARRAY_LIST")
        om.put(mapa, dates, datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry,data)
    return mapa


    #TODO: Crear la función para estructurar los datos
    pass
def compare_elements(keyname, element):
    shootout_entry = me.getKey(element)
    if keyname== shootout_entry:
        return 0
    elif keyname>shootout_entry:
        return 1
    else:
        return -1

# Funciones de consulta
def get_data_5(data_structs,tamano):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista   
    resultados = lt.newList("ARRAY_LIST")
    lt.addFirst(resultados,lt.firstElement(data_structs))
    for b in range(2,6):
        p = lt.getElement(data_structs, b)
        lt.addLast(resultados, p)
    for b in range (0,5):
        p = lt.getElement(data_structs, (tamano-4+b))
        lt.addLast(resultados, p)
    return resultados

def get_data_3(data_structs,tamano):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista   
    resultados = lt.newList("ARRAY_LIST")
    lt.addFirst(resultados,lt.firstElement(data_structs))
    for b in range(2,4):
        p = lt.getElement(data_structs, b)
        lt.addLast(resultados, p)
    for b in range (0,3):
        p = lt.getElement(data_structs, (tamano-2+b))
        lt.addLast(resultados, p)
    return resultados


def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs)
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(analyzer,initialmag, finalmag ):
    """
    Función que soluciona el requerimiento 2
    """
    total=0
    lista= lt.newList("SINGLE_LINKED")
    lst = om.keys(analyzer['temblores_mag'], initialmag, finalmag)
    for lstmag in lt.iterator(lst):
        result= me.getValue(om.get(analyzer['temblores_mag'],lstmag))
        tamano=lt.size(result["By_mag"])
        total+=tamano
        diccionario={"mag":lstmag,"Events":tamano,"Details":lt.newList("ARRAY_LIST")}
        detalles=diccionario["Details"]
        ordenada= merg.sort(result["By_mag"],compare_results_list)
        if tamano<6:
            for cada in lt.iterator(ordenada):
                dato=nuevo(cada)
                lt.addLast(detalles,dato)
        else:
            for b in range(1,4):
                dato = lt.getElement(ordenada, b)
                dato=nuevo(dato)
                lt.addLast(detalles,dato)
            for b in range (0,3):
                dato = lt.getElement(ordenada, (tamano-2+b))
                dato=nuevo(dato)
                lt.addLast(detalles,dato)
        lt.addFirst(lista,diccionario)
    return lista,total
    # TODO: Realizar el requerimiento 2
    pass
def nuevo(cada):
    fecha = datetime.datetime.strptime(cada["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    dates = fecha.strftime('%Y-%m-%d %H:%M:%S')
    dato= {"time":dates,"mag":cada["mag"],"lat":cada["lat"],"long":cada["long"],"depth":cada["depth"],"sig":cada["sig"],"gap":cada["gap"],
           "nst":cada["nst"],"title":cada["title"],"cdi":cada["cdi"],"mmi":cada["mmi"],"magType":cada["magType"],"type": cada["type"],"code":cada["code"]}
    return dato
def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if data_1 == data_2:
        return 0
    elif data_1>data_2:
        return 1
    return -1
def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
    

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass
def compare_results_list(data1, data2):
    fecha1= datetime.datetime.strptime(data1['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_1 = fecha1.strftime('%Y-%m-%d %H:%M:%S')
    fecha2= datetime.datetime.strptime(data2['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
    date_2 = fecha2.strftime('%Y-%m-%d %H:%M:%S')
    if date_1>date_2:
        return 1
    elif date_1==date_2:
        return 0
    else :
        return -1

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
