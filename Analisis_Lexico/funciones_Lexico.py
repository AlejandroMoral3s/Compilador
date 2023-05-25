import re #importando la libreria de REGEX.
from separadores_Lexico import *  #Importando la clase en donde se encuentran los simbolos separadores.


""" [ FUNCIONES DE SEPARACION PARA SIGNOS IMPORTANTES DE PUNTUACION ] """

def separar_por_coma(linea):  #Funcion que proporciona una separacion por comas
    
    contenedor = re.split('(,)', linea) #Separar por caracter y colocando la separacion en una lista, pero conservando el caracter.
    nuevo_string = ' '.join(contenedor) #Uniendo la lista en un STRING separado por espacios
    return nuevo_string #devolviendo el string

def separar_por_espacio(linea):

    contenedor = linea.split()
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_puntoComa(linea):

    contenedor = re.split('(;)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

"""  [ FUNCIONES DE SEPARACION PARA SIGNOS DE AGRUPACION  ]"""

string = '}hola'

def separar_por_parentesis_abierto(linea):
    
    contenedor = re.split('(\()',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_parentesis_cerrado(linea):

    contenedor = re.split('(\))',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_corchete_abierto(linea):

    contenedor = re.split('(\[)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_corchete_cerrado(linea):

    contenedor = re.split('(\])',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_llave_abierta(linea):

    contenedor = re.split('(\{)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_llave_cerrada(linea):

    contenedor = re.split('(\})',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string





