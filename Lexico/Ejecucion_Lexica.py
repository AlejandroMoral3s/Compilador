from Lexico.Funciones_separadoras import *
from Lexico.Diccionario import *
from Lexico.Identificacion_Lexica import *

"""PARTE QUE SEPARA LA LINEA DE TEXTO INGRESADA Y LA DEVUELVE COMO STRING Y COMO UNA LISTA DE ELEMENTOS SEPARADOS"""

#Esta funcion devuelve un STRING con todos los caracteres separados por un ESPACIO
def extraer_string_separado(linea): 

    es_division_exacta = False

    string_volatil = linea # Asignando el valor de la linea ingresada a una variable.
    
    string_volatil = separar_por_coma(string_volatil) # A la variable inicial, se le sustituye con un valor diferente dependiendo de la funcion.

    string_volatil = separar_por_puntoComa(string_volatil)

    string_volatil = separar_por_parentesis_abierto(string_volatil)

    string_volatil = separar_por_parentesis_cerrado(string_volatil)

    string_volatil = separar_por_corchete_abierto(string_volatil)

    string_volatil = separar_por_corchete_cerrado(string_volatil)

    string_volatil = separar_por_llave_abierta(string_volatil)

    string_volatil = separar_por_llave_cerrada(string_volatil)

    string_volatil = separar_por_comillas(string_volatil)

    string_volatil = separar_por_apostrofe(string_volatil)

    string_volatil = separar_por_suma(string_volatil)

    string_volatil = separar_por_resta(string_volatil)

    string_volatil = separar_por_multiplicacion(string_volatil)

    # Si hay mas de una diagonal se tomara como simbolo de division exacta

    if(es_division_exacta == False):
        contador = 0

        for letra in string_volatil:
            if(letra == '/'):
                contador+=1

        if(contador>=2):
            string_volatil = separar_por_divisionExacta(string_volatil)
            es_division_exacta = True
    
    # Si no hay mas de una diagonal se tomara como simbolo de division normal

    if(es_division_exacta == False):
        string_volatil = separar_por_division(string_volatil)


    string_volatil = separar_por_mayor(string_volatil)

    string_volatil = separar_por_menor(string_volatil)

    string_volatil = separar_por_igual(string_volatil)

    string_volatil = separar_por_slash(string_volatil)

    string_volatil = separar_por_espacio(string_volatil)

    return string_volatil # Se devuelve el nuevo valor como un string de los caracteres ya separados

#Esta funcion devuelve una LISTA con todas las separaciones hechas por la funcion anterior
def convertir_string_a_lista(linea):
    
    lista_separada = linea.split()
    return lista_separada

"""PARTE QUE SE ENCARGA DE IDENTIFICAR CADA UNO DE LOS ELEMENTOS DE LA LISTA HACIENDO LA RELACION [SIMBOLO-IDENTIFICADOR]"""
 
def identificar_tokens_lexicos(lista_ingresada):
    
    #Declarando una lista en donde almacenar todos los tokens identificados
    lista_volatil = []

    #Declarando una lista en donde se encuentren todas solo las LLAVES del diccionario general
    diccionario = diccionario_general.keys()

    #creando una variable booleana con valor iniciar FALSE
    coincidencia = False
 
    for x in lista_ingresada:
        for y in diccionario:
            if (y == x):
                lista_volatil.append(diccionario_general[y])
                coincidencia = True

        if(identificar_ids(x)==True and coincidencia == False):
            lista_volatil.append('Identificador')
            coincidencia = True

        if(identificar_numeros(x)==True and coincidencia == False):
            lista_volatil.append('Numero')
            coincidencia = True

        if(coincidencia==False):
            lista_volatil.append("ERROR")

        coincidencia = False

    return lista_volatil


    
