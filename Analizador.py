from Ejecucion_Lexica import *
from Proceso_Sintactico import *

#metodo para juntar cada separacion con su correspondiente identificacion lexica
def juntar_listas(lista_separada, lista_identificada):
    lista_vacia = []
    for x in range(0,len(lista_separada)):
        lista_vacia.append([])
        lista_vacia[x].append(lista_separada[x])
        lista_vacia[x].append(lista_identificada[x])
    
    return lista_vacia



with open('ReceptorLineas.txt', 'r') as f:
    read_data = f.read()
    lineas = read_data.splitlines()
    contador = 1
    for linea in lineas:
        
        """----- ANALISIS LEXICO ---- """

        print(f"\n[ANALISIS LEXICO] ------- LINEA {contador} -------\n")

        string_extraido = extraer_string_separado(linea)
        lista_separada = convertir_string_a_lista(string_extraido)
        lista_identificada = identificar_tokens_lexicos(lista_separada)
        listas_juntas = juntar_listas(lista_separada, lista_identificada)
        print(listas_juntas)

        """----- ANALISIS SINTACTICO ---- """

        print(f"\n[ANALISIS SINTACTICO] --- LINEA {contador} --------\n")

        string_sintactico = expresar_cadena_lexica_identificada(lista_identificada)
        print(string_sintactico)
        existeRegla = False

        for elemento in range(0,len(Listado_Reglas_Sintacticas)):
            if (string_sintactico == Listado_Reglas_Sintacticas[elemento]):
                existeRegla = True

        if (existeRegla==True):
            print("Proceso SINTACTICO finalizado sin ningun error!")
        else:
            print(f"Se encontraron errores sintacticos en la linea [ {contador} ], por favor verificar.")        

        contador+=1
        
    

        
        
        

    

