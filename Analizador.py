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
almacen_nombreContextos = []
almacen_numeroContextos = []

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
       
        errorUnicidad = False
        errorDeclaracion = False

        print(f'\n-----------------------------------------------NO. LINEA: [ {contador_lineas} ] -----------------------------------------------\n')

        print("\033[33m"+f"[ANALISIS LEXICO] \n"+"\033[0m")

        string_extraido = extraer_string_separado(linea)
        lista_separada = convertir_string_a_lista(string_extraido)
        lista_identificada = identificar_tokens_lexicos(lista_separada)
        listas_juntas = juntar_listas(lista_separada, lista_identificada)

        for x in listas_juntas:
            if x[1] != "ERROR":
                print("\033[1;32m"+"SIN ERRORES!"+"\033[0m")
                break
            else:
                print("\033[1;31m"+"SE ENCONTRARON ERRORES LEXICOS EN LA LINEA ACTUAL"+"\033[0m")
                break

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


        print("\033[33m"+f"\n[ANALISIS SINTACTICO] \n"+"\033[0m")

        string_sintactico = expresar_cadena_lexica_identificada(lista_identificada)
        existeRegla = False

        for elemento in range(0,len(Listado_Reglas_Sintacticas)):
            if (string_sintactico == Listado_Reglas_Sintacticas[elemento]):
                existeRegla = True

        if (existeRegla==True):
            print("\033[1;32m"+"SIN ERRORES!\n"+"\033[0m")
        else:
            print("\033[1;31m"+"SE ENCONTRARON ERRORES SINTACTICOS EN LA LINEA ACTUAL"+"\033[0m")   



        """-------------------------------------------------------------------------------------------------------------- """
        """------------------------------------------ ANALISIS SEMANTICO ------------------------------------------------ """
        """-------------------------------------------------------------------------------------------------------------- """

        print("\033[33m"+f"\n[ANALISIS SEMANTICO] \n"+"\033[0m")

        # Extrayendo identificadore y tipo de las variables mostradas en DECLARACIONES sin valor

        Id_y_tipo = extraer_identificadores_declaraciones(lista_separada, lista_identificada)

        # Extrayendo identificadores y valores encontradas en ASIGNACIONES

        Id_y_valor = extraer_valor_de_variables(lista_separada, lista_identificada, nombre_contexto, contador_contexto)

        # Creacion de objetos en donde se almacenan los identificadores y que forman parte de DECLARACIONES
        if Id_y_tipo[0] != '':
            for x in Id_y_tipo[1]:

                if contador_contexto == 0:

                    #proceso de solo identificadores
                    objetoVolatil = IdentificadorD(identificador=x, tipo=Id_y_tipo[0],contexto=contador_contexto, idContexto=contador_idContexto, linea=contador_lineas)
                    nombre_contexto = 'principal'
                    
                    #COMPROBACION DE ERRORES DE UNICIDAD
                    if errorUnicidad != True:
                        errorUnicidad = comprobacionUnicidad(objetosId, objetoVolatil)

                    objetosId.append(objetoVolatil)

                else:
                
                    objetoVolatil = IdentificadorD(identificador=x, tipo=Id_y_tipo[0],contexto=contador_contexto, nombreContexto=nombre_contexto, idContexto=contador_idContexto, linea=contador_lineas)

                    #COMPROBACION DE ERRORES DE UNICIDAD
                    if errorUnicidad != True:
                        errorUnicidad = comprobacionUnicidad(objetosId, objetoVolatil)

                    objetosId.append(objetoVolatil)

                contador_idContexto+=1


        #Distribuyendo en arrays por aparte cada atributo de los identificadores de asignacion
        
        if len(Id_y_valor[0]) != 0:

            #Creacion de objetos corespondientes a los identificadores encontrados en ASIGNACIONES
            for x in Id_y_valor[0]:

                if contador_contexto == 0:
                    objetosAsignacion.append(IdentificadorA(x, contexto=contador_contexto))
                    nombre_contexto = 'principal'
                                
                else:
                    objetosAsignacion.append(IdentificadorA(x, nombreContexto=nombre_contexto, contexto=contador_contexto))

            
            if errorDeclaracion != True:
                if len(objetosId) == 0 and len(objetosAsignacion) != 0:
                    errorDeclaracion = True
                elif len(objetosId) != 0 and len(objetosAsignacion) != 0:
                    contadorV = 0
                    for i in objetosAsignacion:
                        for j in objetosId:
                            if i.identificador == j.identificador:
                                contadorV += 1
                    
                    if contadorV == 0:
                        errorDeclaracion = True
                    else:
                        for i in objetosAsignacion:
                            for j in objetosId:
                                if i.identificador == j.identificador and i.contexto == j.contexto and i.nombreContexto == j.nombreContexto:
                                    errorDeclaracion = False
                                    
                                elif i.identificador == j.identificador and j.contexto < i.contexto and i.nombreContexto != j.nombreContexto:
                                    errorDeclaracion = False
                                    
                                else:
                                    errorDeclaracion = True
                                    
                      
        #COLOCANDO ATRIBUTOS DE CADA VARIABLE ENCONTRADA EN ASIGNACION DENTRO DE SUS RESPECTIVOS ARRAYS

        for i in range(0, len(Id_y_valor[0])):
            almacen_ids_asignacion.append(Id_y_valor[0][i])
            almacen_valores_asignacion.append(Id_y_valor[1][i])
            almacen_tipo_valores.append(Id_y_valor[2][i])
            almacen_dimensiones.append(Id_y_valor[3][i])
            almacen_nombreContextos.append(Id_y_valor[4][i])
            almacen_numeroContextos.append(Id_y_valor[5][i])


        #COMPROBANDO ERRORES DE UNICIDAD Y DECLARACION

        if errorUnicidad and errorDeclaracion:
            print("\033[1;31m"+"ERROR DE UNICIDAD Y DECLARACION EN ESTA LINEA\n"+"\033[0m")
        elif errorUnicidad and not(errorDeclaracion):
            print("\033[1;31m"+"ERROR DE UNICIDAD EN ESTA LINEA\n"+"\033[0m")
        elif errorDeclaracion and not(errorUnicidad):
            print("\033[1;31m"+"ERROR DE DECLARACION EN ESTA LINEA\n"+"\033[0m")
        else:
            print("\033[1;32m"+"SIN ERRORES DE UNICIDAD Y DECLARACION!\n"+"\033[0m")


        print("\033[35m"+'=================================================================================================================='+"\033[0m")

        contador_lineas+=1


    asignar_nuevos_valores(
        objetosId, 
        almacen_ids_asignacion, 
        almacen_valores_asignacion, 
        almacen_tipo_valores,
        almacen_dimensiones,
        almacen_nombreContextos,
        almacen_numeroContextos
        )

    print("\033[33m"+f"\n[OTROS POSIBLES ERRORES EN ANALISIS SEMANTICO: ] \n"+"\033[0m")

    errorChequeoTipos = 0
    advertenciaInicializacion = 0

    for x in objetosId:

        if x.tipo == 'entero' and x.valor == 'null':
            advertenciaInicializacion +=1
            x.valor = '0'
            x.tipoValor = 'entero'
            x.dimension = '0'
        elif x.tipo == 'doble' and x.valor == 'null':
            advertenciaInicializacion +=1
            x.valor = '0.0'
            x.tipoValor = 'doble'
            x.dimension = '0.0'
        elif x.tipo == 'cadena' and x.valor == 'null':
            advertenciaInicializacion +=1
            x.valor = ''
            x.tipoValor = 'cadena'
            x.dimension = '0'
        elif x.tipo == 'caracter' and x.valor == 'null':
            advertenciaInicializacion +=1
            x.valor = ''
            x.tipoValor = 'caracter'
            x.dimension = '0'
            

        if x.tipo != x.tipoValor:
            errorChequeoTipos+=1


    if errorChequeoTipos == 0:
        if advertenciaInicializacion != 0:
            print("\033[1;32m"+f"[ADVERTENCIA]: Se inicializaron automaticamente [ {advertenciaInicializacion} ] variables.\n"+"\033[0m")
        print("\033[1;32m"+"SIN ERRORES DE CHEQUEO DE TIPO!\n"+"\033[0m")
    
    else:  
        print("\033[1;31m"+"EXISTEN ERRORES DE CHEQUEO DE TIPOS\n"+"\033[0m")  


    for x in objetosId:
        print(x)

    
    
    

    

