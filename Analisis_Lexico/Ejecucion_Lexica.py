from Funciones_separadoras import *


linea_de_texto = '    int hola = 1;'


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

    string_volatil = separar_por_str(string_volatil)

    string_volatil = separar_por_int(string_volatil)

    string_volatil = separar_por_char(string_volatil)

    string_volatil = separar_por_float(string_volatil)
    
    string_volatil = separar_por_if(string_volatil)

    string_volatil = separar_por_for(string_volatil)

    string_volatil = separar_por_while(string_volatil)

    string_volatil = separar_por_espacio(string_volatil)

    return string_volatil # Se devuelve el nuevo valor como un string de los caracteres ya separados

#Esta funcion devuelve una LISTA con todas las separaciones hechas por la funcion anterior
def convertir_string_a_lista(linea):
    
    lista_separada = linea.split()
    return lista_separada


string_extraido = extraer_string_separado(linea_de_texto)

lista = convertir_string_a_lista(string_extraido)

print(string_extraido)
print(lista)
    
