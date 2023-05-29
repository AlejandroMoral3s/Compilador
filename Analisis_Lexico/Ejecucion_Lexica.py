from Funciones_separadoras import *
from Diccionario import *
from Identificacion_Lexica import *

linea_de_texto = 'hola{,;}'

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

string_extraido = extraer_string_separado(linea_de_texto)

lista = convertir_string_a_lista(string_extraido)

"""PARTE QUE SE ENCARGA DE IDENTIFICAR CADA UNO DE LOS ELEMENTOS DE LA LISTA HACIENDO LA RELACION [SIMBOLO-IDENTIFICADOR]"""

# HAY QUE REVISAR ESTE METODO, NO ESTA COMPLETO Y ES DISFUNCIONAL 
def identificar_tokens_lexicos(lista_ingresada):
    
    #Declarando una lista en donde almacenar todos los tokens identificados
    lista_volatil = []

    #Declarando una lista en donde se encuentren todas solo las LLAVES del diccionario general
    diccionario = diccionario_general.keys()

    #creando una variable booleana con valor iniciar FALSE
    coindicencia = False

    """El primer ciclo evalua cada uno de los elementos de la lista separada previamente por
    CONVERTIR_STRING_A_LISTA, el seugndo ciclo evalua cada uno de los elementos que se tienen en 
    DICCIONARIO_GENERAL, dentro de ellos se encuentra un condicional que evalua si el elemento que 
    se encuentra evaluandose en ese momento en ambos bucles es IGUAL, si lo es, entonces agrega
    el valor que contiene el elemento(llave) que se esta evaluando en ese instante, y la variable
    booleana se convierte en TRUE, cuando termina el ciclo de segundo nivel y se entra al segundo
    condicional, este evalua si la variable booleana es FALSE (eso significaria que no se encontro
    ninguna coincidencia dentro de las llaves del diccionario), de ser asi, agrega un texto de error
    a la lista de identificadores. Por ultimo se hace que la variable vuelva a su estado original,
    para que el proceso pueda repetirse nuevamente."""
 
    for x in lista_ingresada:
        for y in diccionario:
            if (y == x):
                lista_volatil.append(diccionario_general[y])
                coindicencia = True
            
        if(coindicencia==False):
            lista_volatil.append("ERROR")

        coindicencia = False

    return lista_volatil



print(string_extraido)
print(lista)
print(identificar_tokens_lexicos(lista))
    
