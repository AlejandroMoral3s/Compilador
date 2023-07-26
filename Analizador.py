from Ejecucion_Lexica import *
from Proceso_Sintactico import *
from objetoIdentificador import *
from objetoIdAsignacion import *


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
objetosAsignacion = []

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
            objetosId.append(IdentificadorD(identificador=x, tipo=Id_y_tipo[0],contexto=contador_contexto, nombreContexto=nombre_contexto, idContexto=contador_idContexto, linea=contador_lineas))
            contador_idContexto+=1


        # Extrayendo identificadores y valores encontradas en ASIGNACIONES

        Id_y_valor = extraer_valor_de_variables(lista_separada, lista_identificada)

        #Distribuyendo en arrays por aparte cada atributo de los identificadores de asignacion
        for i in range(0, len(Id_y_valor[0])):
            almacen_ids_asignacion.append(Id_y_valor[0][i])
            almacen_valores_asignacion.append(Id_y_valor[1][i])
            almacen_tipo_valores.append(Id_y_valor[2][i])
            almacen_dimensiones.append(Id_y_valor[3][i])

        #Creacion de objetos corespondientes a los identificadores encontrados en ASIGNACIONES
        for x in Id_y_valor[0]:
            objetosAsignacion.append(IdentificadorA(x, nombreContexto=nombre_contexto, contexto=contador_contexto, linea=contador_lineas))


        contador_lineas+=1


    print(f"\n[ANALISIS SEMANTICO] ----------\n")

    #EN PROCESO: asignacion de valores correspondientes
    #asignar_nuevos_valores(objetosId, almacen_ids_asignacion, almacen_valores_asignacion, almacen_tipo_valores, almacen_dimensiones)

    errorUnicidad = False
    errorDeclaracion = False

    #CODIGO PARA VALIDAR LOS ERRORES DE UNICIDAD ---------------------------------------------------------------------

    idsD = []
    contextoD = []
    nContextoD = []

    for x in objetosId:
        idsD.append(x.identificador)
        contextoD.append(x.contexto)
        nContextoD.append(x.nombreContexto)

    if len(idsD) != len(set(idsD)) and len(contextoD) != len(set(contextoD)) and len(nContextoD) != len(set(nContextoD)):
        errorUnicidad = True

    print(idsD)
    print(contextoD)
    print(nContextoD)

    #CODIGO PARA VALIDAR LOS ERRORES DE DECLARACION -------------------------------------------------------------------

    if len(objetosId) == 0 and len(objetosAsignacion) !=0:
        errorDeclaracion = True
    
    if errorDeclaracion == False:
        for x in objetosAsignacion:
            for y in objetosId:
                if x.identificador == y.identificador and x.linea < y.linea :
                    errorDeclaracion = True
                elif x.identificador == y.identificador and x.contexto == y.contexto and x.nombreContexto != y.nombreContexto:
                    errorDeclaracion = True


    #CONCLUYENDO EL ANALISIS SEMANTICO

    if errorDeclaracion and errorUnicidad:
        print("EXISTEN ERRORES DE TIPO: [ DECLARACION ] y [ UNICIDAD ], por favor verificar.")
    elif errorUnicidad and not(errorDeclaracion):
        print("EXISTE UN ERROR DE TIPO: [ UNICIDAD ], por favor verificar.")
    elif errorDeclaracion and not(errorUnicidad):
        print("EXISTE UN ERROR DE TIPO: [ DECLARACION ], por favor verificar.")
    else:
        print("ANALISIS SEMANTICO FINALIZADO SIN NINGUNA COMPLICACION! :D")
    
    print('')

    # Mostrando OBJETOS EN OBJETOS DECLARACION Y ASIGNACION
     
    """for x in objetosId:
        print(x)
    
    print('')

    for x in objetosAsignacion:
        print(x)"""
        
        
        

    

