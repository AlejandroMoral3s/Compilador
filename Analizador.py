from Ejecucion_Lexica import *
from Proceso_Sintactico import *
from objeto_id_asig import *
from metodosSemanticos import *

#ABRIENDO ARCHIVO PARA EL ANALISIS
with open('ReceptorLineas.txt', 'r') as f:
    
    read_data = f.read()
    lineas = read_data.splitlines()

    contador_lineas = 1
    contador_contexto = 0
    nombre_contexto = 'principal'

    objetosVariableDeclaracion = []
    objetosVariableAsignacion = []

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


        """Si se encuentra una apertura de metodo y un cierre del mismo, se procede a aumentar o disminuir contador de
        contextos"""

        for x in range(0, len(lista_identificada)):
            if lista_identificada[x] == 'Identificador' and lista_identificada[x+1] == 'llave abierta' :
                nombre_contexto = lista_separada[x]
                contador_contexto+=1
            elif lista_identificada[x] == "llave cerrada":
                contador_contexto-=1


        """-------------------------------------------------------------------------------------------------------------- """
        """------------------------------------------ ANALISIS SINTACTICO ----------------------------------------------- """
        """-------------------------------------------------------------------------------------------------------------- """

        print(f"\n[ANALISIS SINTACTICO] --- LINEA {contador_lineas} --------\n")

        string_sintactico = expresar_cadena_lexica_identificada(lista_identificada) #String con elementos identificados
        existeRegla = False

        for elemento in range(0,len(Listado_Reglas_Sintacticas)):
            if (string_sintactico == Listado_Reglas_Sintacticas[elemento]):
                existeRegla = True       


        """-------------------------------------------------------------------------------------------------------------- """
        """------------------------------------------ ANALISIS SEMANTICO ------------------------------------------------ """
        """-------------------------------------------------------------------------------------------------------------- """
    
        # PROCESO EXCLUSIVO PARA DECLARACIONES DE VARIABLES Y ASIGNACION DE LAS MISMAS CON SUS RESPECTIVOS VALORES INICIALES
        
        #------------------------------------------------------------------------------------------------------------------
        
        variableDeclaradaLineaActual = extraer_declaracion_variables(string_sintactico, lista_identificada, lista_separada)
        
        #Creando objeto individual de una variable declarada

        if variableDeclaradaLineaActual != 0:
            objetosVariableDeclaracion.append(Identificador(
                variableDeclaradaLineaActual[1],
                variableDeclaradaLineaActual[2],
                contador_contexto,
                contador_lineas,
                nombre_contexto,
                variableDeclaradaLineaActual[0],
                variableDeclaradaLineaActual[3]
            ))
               
        #Asegurando que en todos los objetos en contexto cero se coloque el nombre PRINCIPAL
        for x in objetosVariableDeclaracion:
            if x.numeroContexto == 0:
                x.nombreContexto = 'principal'

        #------------------------------------------------------------------------------------------------------------------

        currStringAsig = extraer_asignacion_variables(string_sintactico, lista_separada)
        
        if currStringAsig != 0:
            objCurrAsig = Asignador(
                currStringAsig[1], currStringAsig[2], contador_contexto, nombre_contexto, currStringAsig[3])
            objetosVariableAsignacion.append(objCurrAsig)

            for x in objetosVariableAsignacion:
                if x.numeroContexto == 0:
                    x.nombreContexto = 'principal'

            for x in objetosVariableDeclaracion:
                if ((x.identificador == objCurrAsig.identificador) and (x.nombreContexto == objCurrAsig.nombreContexto) and (currStringAsig[0] == '')):
                    x.valor = objCurrAsig.valor
                    x.tipoAsig = objCurrAsig.tipoAsig

                elif((x.identificador == objCurrAsig.identificador) and (x.nombreContexto == 'principal') and (currStringAsig[0] == '0')):
                    
                    x.valor = objCurrAsig.valor
                    x.tipoAsig = objCurrAsig.tipoAsig
            
            

        contador_lineas+=1


for x in objetosVariableDeclaracion:
    print(x)
        
        
        

    

