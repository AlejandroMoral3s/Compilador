from Lexico.Ejecucion_Lexica import *
from Sintactico.Proceso_Sintactico import *
from Semantico.ObjetosTS import *

#metodo para juntar cada separacion con su correspondiente identificacion lexica
def juntar_listas(lista_separada, lista_identificada):
    lista_vacia = []
    for x in range(0,len(lista_separada)):
        lista_vacia.append([])
        lista_vacia[x].append(lista_separada[x])
        lista_vacia[x].append(lista_identificada[x])
    
    return lista_vacia

#Almacen  de todos los objetos identificador que se lleguen a crear
objetos_Identificador = []


with open('ReceptorLineas.txt', 'r') as f:
    read_data = f.read()
    lineas = read_data.splitlines()
    contador = 1
    for linea in lineas:
        
        """--------------------------------- ANALISIS LEXICO ------------------------------------------------------- """


        print(f"\n[ANALISIS LEXICO] ------- LINEA {contador} -------\n")

        string_extraido = extraer_string_separado(linea) #Esta linea devuelve la linea (COMO STRING) ya separada por los caracteres
        lista_separada = convertir_string_a_lista(string_extraido) #Esta linea devuelve la linea separada como una lista
        lista_identificada = identificar_tokens_lexicos(lista_separada) #Esta linea devuelve la lista de separaciones a una lista de tokens
        listas_juntas = juntar_listas(lista_separada, lista_identificada) # Esta linea se encarga de juntar la lista de separaciones con la de tokens
        print(listas_juntas)



        """--------------------------------- ANALISIS SINTÁCTICO ------------------------------------------------------- """


        print(f"\n[ANALISIS SINTACTICO] --- LINEA {contador} --------\n")

        string_sintactico = expresar_cadena_lexica_identificada(lista_identificada)
        print(string_sintactico)
        existeRegla = False

        for elemento in range(0,len(Listado_Reglas_Sintacticas)):
            if (string_sintactico == Listado_Reglas_Sintacticas[elemento]):
                existeRegla = True

        if (existeRegla==True):
            print("Proceso SINTACTICO finalizado sin ningun error!\n")
        else:
            print(f"Se encontraron errores sintacticos en la linea [ {contador} ], por favor verificar.\n")     



        """--------------------------------- ANALISIS SEMANTICO ------------------------------------------------------- """


        #Extrayendo identificadores, tipos y dimensiones en una sola lista
        id_tipo_dimension = devolver_id_y_tipo(lista_separada, lista_identificada)
                
        #clasificando en distintas listas los ids, tipos y dimensiones para un mejor orden y manejo
        ids = id_tipo_dimension[0]
        tipos = id_tipo_dimension[1]
        dimensiones = id_tipo_dimension[2]

        for i in range(0, len(ids)):

            objetoVolatil = Identificador(ids[i], tipos[i], dimensiones[i])
            objetos_Identificador.append(objetoVolatil)

    
        contador+=1

    for i in objetos_Identificador:
        print(i)   
    

        
        
        

    

