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
    mag = data['mag']
    entry = om.get(mapa, mag)
    if entry is None:
        datentry = new_data()
        om.put(mapa,mag, datentry)
    else:
        datentry = me.getValue(entry)
    add_data(datentry, data)
    return mapa
#def updateDate(mapa, data):
    occurreddate = data['time']
    fecha = datetime.datetime.strptime(occurreddate, "%Y-%m-%dT%H:%M:%S.%fZ")
    dates = fecha.strftime('%Y-%m-%dT%H:%M')
    entry = om.get(mapa, dates)
    if entry is None:
        datentry = new_data()
        om.put(mapa, dates, datentry)
    else:
        datentry = me.getValue(entry)
    add_data(datentry, data)
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
    data["By_depth"]=mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compare_elements)
    return data
def add_data(structs,data):
    mapa= structs["By_depth"]
    entry= mp.get(mapa,data["depth"])
    if entry:
        lista= me.getValue(entry)
    else:
        lista= lt.newList("ARRAY_LIST")
        mp.put(mapa,data["depth"],lista)
    lt.addLast(lista,data)
    return structs


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


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
