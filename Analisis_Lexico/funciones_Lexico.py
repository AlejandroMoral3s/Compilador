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

"""  [ FUNCIONES DE SEPARACION PARA CADENAS Y CARACTERES  ]"""

def separar_por_comillas(linea):

    contenedor = re.split('(\")',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_apostrofe(linea):

    contenedor = re.split('(\')',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

"""  [ FUNCIONES DE SEPARACION PARA SIMBOLOS MATEMATICOS  ]"""

def separar_por_suma(linea):

    contenedor = re.split('(\+)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_resta(linea):

    contenedor = re.split('(\-)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_multiplicacion(linea):

    contenedor = re.split('(\*)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_division(linea):

    contenedor = re.split('(/)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_divisionExacta(linea):

    contenedor = re.split('(//)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_modulo(linea):

    contenedor = re.split('(%)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_mayor(linea):

    contenedor = re.split('(>)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_menor(linea):

    contenedor = re.split('(<)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_igual(linea):

    contenedor = re.split('(=)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

"""  [ FUNCIONES DE SEPARACION PARA COMENTARIOS DE UNA LINEA  ]"""

def separar_por_slash(linea):

    contenedor = re.split('(#)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

"""  [ FUNCIONES DE SEPARACION PARA PALABRAS RESERVADAS  ]"""

string = "string hola"

def separar_por_str(linea):

    contenedor = re.split('(str)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_int(linea):

    contenedor = re.split('(int)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_char(linea):

    contenedor = re.split('(char)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_float(linea):

    contenedor = re.split('(float)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_if(linea):

    contenedor = re.split('(if)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_for(linea):

    contenedor = re.split('(for)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string

def separar_por_while(linea):

    contenedor = re.split('(while)',linea)
    nuevo_string = ' '.join(contenedor)
    return nuevo_string






