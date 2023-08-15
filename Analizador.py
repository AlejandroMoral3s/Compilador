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
        #------------------------------------------------------------------------------------------------------------------

        #variable lista, que almacena los atributos de la variable actual declarada
        variableDeclaradaLineaActual = extraer_declaracion_variables(string_sintactico, lista_identificada, lista_separada)

        contadorRepeticiones = 0
        #Creando objeto individual de una variable declarada

        if variableDeclaradaLineaActual != 0:
            #creando el objeto de la variable declarada en la linea actual
            objCurrDec = Identificador(
                variableDeclaradaLineaActual[1],
                variableDeclaradaLineaActual[2],
                contador_contexto,
                contador_lineas,
                nombre_contexto,
                variableDeclaradaLineaActual[0],
                variableDeclaradaLineaActual[3]
            )
               
            #verificando que la variable no exista en el mismo contexto, no tenga el mismo nombre y que no tenga el mismo numero de contexto
            for x in objetosVariableDeclaracion:
                if (x.identificador == objCurrDec.identificador) and (x.nombreContexto == objCurrDec.nombreContexto) and (x.numeroContexto == objCurrDec.numeroContexto):
                    contadorRepeticiones += 1

            #Si hay alguna repeticion detiene la ejecucion abruptamente
            if contadorRepeticiones != 0:
                print('ERROR DE UNICIDAD, LA VARIABLE YA SE HA DECLARADO ANTES.')
                break
            
            #DECLARACION DE VARIABLES CON CONTENIDO DE OTRAS VARIABLES
            if objCurrDec.tipoAsig == 'VarVar':
                for y in objetosVariableDeclaracion:
                    if (y.identificador == objCurrDec.valor) and (y.nombreContexto == objCurrDec.nombreContexto):
                        objCurrDec.valor = y.valor
                        objCurrDec.tipoAsig = y.tipoAsig
                    elif (y.identificador != objCurrDec.valor) and (y.nombreContexto == objCurrDec.nombreContexto):
                        continue

            elif objCurrDec.tipoAsig == 'VarVarClass':
                for y in objetosVariableDeclaracion:
                    if (y.identificador == objCurrDec.valor) and (y.nombreContexto == 'principal'):
                        objCurrDec.valor = y.valor
                        objCurrDec.tipoAsig = y.tipoAsig
                    elif (y.identificador != objCurrDec.valor) and (y.nombreContexto == 'principal'):
                        continue

            if (objCurrDec.tipoAsig == 'VarVar') or (objCurrDec.tipoAsig == 'VarVarClass'):
                print('ERROR DE DECLARACION, LA VARIABLE AUN NO SE HA DECLARADO.')
                #cortando ejecucion de programa abruptamente
                break
            else:
                #luego se almacena la variable 
                objetosVariableDeclaracion.append(objCurrDec)

        #Asegurando que en todos los objetos en contexto cero se coloque el nombre PRINCIPAL
        for x in objetosVariableDeclaracion:
            if x.numeroContexto == 0:
                x.nombreContexto = 'principal'

        #------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------------

        #metodo que permite extraer los atributos de la variable a la cual se busca realizar una asignacion
        currStringAsig = extraer_asignacion_variables(string_sintactico, lista_separada) # [entorno, variable, valor, tipoValor]
        
        #Contador que permite saber si hay errores de declaracion
        contadorCoincidencias = 0
        esTipoAsignacionVarVar = False
        esTipoAsigVarVarClass = False

        if currStringAsig != 0:
            #Instanciando objeto asignador para la variable en linea actual
            objCurrAsig = Asignador(
                currStringAsig[1], currStringAsig[2], contador_contexto, nombre_contexto, currStringAsig[3])
            #Aniadiendo el objeto recien creado a una lista de variables de asignacion
            objetosVariableAsignacion.append(objCurrAsig)

            #asegurandonos que todos los objetos de DECLARACION que tengan como contexto 0 reciban el nombre de 'principal'
            for x in objetosVariableAsignacion:
                if x.numeroContexto == 0:
                    x.nombreContexto = 'principal'

            for x in objetosVariableDeclaracion:
                #comparando que la asignacion actual y algun objeto de la lista de Declaraciones, tengan mismo nombre, mismo nombre de contexto y un entorno diferente de 0
                if ((x.identificador == objCurrAsig.identificador) and (x.nombreContexto == objCurrAsig.nombreContexto) and (currStringAsig[0] == '')):
                        
                    contadorCoincidencias += 1
                    x.valor = objCurrAsig.valor
                    x.tipoAsig = objCurrAsig.tipoAsig

                    if objCurrAsig.tipoAsig == "VarVar":
                        for i in objetosVariableDeclaracion:
                            if i.identificador == objCurrAsig.valor:
                                x.valor = i.valor
                                x.tipoAsig = i.tipoAsig

                #Comparando que se tenga mismo nombre, que el contexto sea 'principal' y que el entorno sea 0
                elif((x.identificador == objCurrAsig.identificador) and (x.nombreContexto == 'principal') and (currStringAsig[0] == '0')):
                        
                    contadorCoincidencias += 1
                    x.valor = objCurrAsig.valor
                    x.tipoAsig = objCurrAsig.tipoAsig
            
                    if objCurrAsig.tipoAsig == "VarVarClass":
                        for i in objetosVariableDeclaracion:
                            if i.identificador == objCurrAsig.valor:
                                x.valor = i.valor
                                x.tipoAsig = i.tipoAsig

            for x in objetosVariableDeclaracion:
                if x.tipoAsig == 'VarVar':
                    esTipoAsignacionVarVar = True
                    break
                elif x.tipoAsig == 'VarVarClass':
                    esTipoAsigVarVarClass = True
                    break

            #Lanzando error de DECLARACION!
            if contadorCoincidencias == 0 or esTipoAsignacionVarVar == True or esTipoAsigVarVarClass == True:
                
                print('ERROR DE DECLARACION, LA VARIABLE AUN NO SE HA DECLARADO.')
                #cortando ejecucion de programa abruptamente
                break
        
        #------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------------

        tiposCoincidentes = False
        listaChequeoImplicito = comparacionTipos(objetosVariableDeclaracion[-1])
        tiposCoincidentes = listaChequeoImplicito[0]
        objetosVariableDeclaracion[-1].valor = listaChequeoImplicito[1]
        objetosVariableDeclaracion[-1].tipoAsig = listaChequeoImplicito[2]

        for x in objetosVariableDeclaracion:
            if x.tipoDec == 'caracter' and x.tipoAsig == 'entero':
                x.valor = chr(int(x.valor))
            elif x.tipoDec == 'caracter' and x.tipoAsig == 'doble':
                valorTruncado = ''
                for letra in x.valor:
                    if letra != '.': 
                        valorTruncado+=letra
                    else:
                        break
                x.valor = chr(int(valorTruncado))

        if not(tiposCoincidentes):
            print('ERROR EN CHEQUEO DE TIPOS')
            break

        contador_lineas+=1


for x in objetosVariableDeclaracion:
    print(x)
        
        
        

    

