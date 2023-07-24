from Ejecucion_Lexica import *
from Proceso_Sintactico import *
from objetoIdentificador import *


#metodo para juntar cada separacion con su correspondiente identificacion lexica

def juntar_listas(lista_separada, lista_identificada):
    lista_vacia = []
    for x in range(0,len(lista_separada)):
        lista_vacia.append([])
        lista_vacia[x].append(lista_separada[x])
        lista_vacia[x].append(lista_identificada[x])
    
    return lista_vacia

#ALMACEN DE OBJETOS IDENTIFICADORES PARA DECLARACIONES
objetosId = []

#ALMACEN PARA IDENTIFICADORES Y VALORES ENCONTRADOS EN ASIGNACION
almacen_ids_asignacion = []
almacen_valores_asignacion = []
almacen_tipo_valores = []
almacen_dimensiones = []

#ABRIENDO ARCHIVO PARA EL ANALISIS
with open('ReceptorLineas.txt', 'r') as f:
    
    read_data = f.read()
    lineas = read_data.splitlines()

    contador_lineas = 1
    contador_contexto = 0
    contador_idContexto = 0
    nombre_contexto = 'principal'

    
    #Comenzando el analisis por linea individual

    for linea in lineas:
        
        """-------------------------------------------------------------------------------------------------------------- """
        """------------------------------------------ ANALISIS LEXICO --------------------------------------------------- """
        """-------------------------------------------------------------------------------------------------------------- """
       
        print(f"\n[ANALISIS LEXICO] ------- LINEA {contador_lineas} -------\n")

        string_extraido = extraer_string_separado(linea)
        lista_separada = convertir_string_a_lista(string_extraido)
        lista_identificada = identificar_tokens_lexicos(lista_separada)
        listas_juntas = juntar_listas(lista_separada, lista_identificada)
        print(listas_juntas)


        #MODIFICANDO EL CONTADOR CONTEXTO 

        for x in range(0, len(lista_identificada)):
            if lista_identificada[x] == "Identificador" and lista_identificada[x+1] == "llave abierta":
                nombre_contexto = lista_separada[x]
                contador_contexto+=1
            elif lista_identificada[x] == "llave cerrada":
                contador_contexto-=1


        """-------------------------------------------------------------------------------------------------------------- """
        """------------------------------------------ ANALISIS SINTACTICO ----------------------------------------------- """
        """-------------------------------------------------------------------------------------------------------------- """

        print(f"\n[ANALISIS SINTACTICO] --- LINEA {contador_lineas} --------\n")

        string_sintactico = expresar_cadena_lexica_identificada(lista_identificada)
        print(string_sintactico)
        existeRegla = False

        for elemento in range(0,len(Listado_Reglas_Sintacticas)):
            if (string_sintactico == Listado_Reglas_Sintacticas[elemento]):
                existeRegla = True

        if (existeRegla==True):
            print("Proceso SINTACTICO finalizado sin ningun error!\n")
        else:
            print(f"Se encontraron errores sintacticos en la linea [ {contador_lineas} ], por favor verificar.\n")        


        """-------------------------------------------------------------------------------------------------------------- """
        """------------------------------------------ ANALISIS SEMANTICO ------------------------------------------------ """
        """-------------------------------------------------------------------------------------------------------------- """


        # Extrayendo identificadore y tipo de las variables mostradas en DECLARACIONES sin valor

        Id_y_tipo = extraer_identificadores_declaraciones(lista_separada, lista_identificada)
        

        # Creacion de objetos en donde se almacenan los identificadores y que forman parte de declaraciones

        for x in Id_y_tipo[1]:
            objetosId.append(Identificador(identificador=x, tipo=Id_y_tipo[0],contexto=contador_contexto, nombreContexto=nombre_contexto, idContexto=contador_idContexto, linea=contador_lineas))
            contador_idContexto+=1


        # Extrayendo identificadores y valores encontradas en ASIGNACIONES

        Id_y_valor = extraer_valor_de_variables(lista_separada, lista_identificada)

        for i in range(0, len(Id_y_valor[0])):
            almacen_ids_asignacion.append(Id_y_valor[0][i])
            almacen_valores_asignacion.append(Id_y_valor[1][i])
            almacen_tipo_valores.append(Id_y_valor[2][i])
            almacen_dimensiones.append(Id_y_valor[3][i])

        contador_lineas+=1

    
    asignar_nuevos_valores(objetosId, almacen_ids_asignacion, almacen_valores_asignacion, almacen_tipo_valores, almacen_dimensiones)


    print(almacen_valores_asignacion)
    print(almacen_ids_asignacion)
    print(almacen_tipo_valores)
    print(almacen_dimensiones)

    for x in objetosId:
        print(x)
    

        
        
        

    

