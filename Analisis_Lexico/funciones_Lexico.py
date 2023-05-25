import re #importando la libreria de REGEX.
from separadores_Lexico import *  #Importando la clase en donde se encuentran los simbolos separadores.

string = 'hola,      como,       estas'

def separar_por_coma(linea):  #Funcion que proporciona una separacion por comas
    
    contenedor = re.split('(,)', linea) #Separar por comas y colocando la separacion en una lista, pero conservando el caracter.
    nuevo_string = ' '.join(contenedor) #Uniendo la lista en un STRING separado por espacios
    return nuevo_string #devolviendo el string

def separar_por_espacio(linea):

    contenedor = linea.split()
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

print(separar_por_espacio(separar_por_coma(string)))



