import re #importando la libreria de REGEX.
from separadores_Lexico import *  #Importando la clase en donde se encuentran los simbolos separadores.

string = 'hola,      como,       estas'

def separar_por_coma(linea):
    
    contenedor = re.split('(,)', linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_espacio(linea):

    contenedor = linea.split()
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

print(separar_por_espacio(separar_por_coma(string)))



