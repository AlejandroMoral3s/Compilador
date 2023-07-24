class Identificador:

    def __init__(self, identificador, tipo, valor = 'null', tipoValor = 'null', nombreContexto = 'principal', contexto = 0, idContexto=0, linea=0, dimension='null'):
        self.__identificador = identificador
        self.__tipo = tipo
        self.__valor = valor
        self.__tipoValor = tipoValor
        self.__nombreContexto = nombreContexto
        self.__contexto = contexto
        self.__idContexto = idContexto
        self.__linea = linea
        self.__dimension = dimension

    # Creando metodos GET Y SET para el identificador

    @property
    def identificador(self):
        return self.__identificador
    
    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    # Creando metodos GET Y SET para el tipo de declaracion

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    # Creando metodos GET Y SET para el valor del identificador en asignacion

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    # Creando metodos GET Y SET para el tipo de valor asignado

    @property
    def tipoValor(self):
        return self.__tipoValor
    
    @tipoValor.setter
    def tipoValor(self, tipoValor):
        self.__tipoValor = tipoValor

    # Creando metodos GET Y SET para el nombre de contexto asignado

    @property
    def nombreContexto(self):
        return self.__nombreContexto
    
    @nombreContexto.setter
    def nombreContexto(self, nombreContexto):
        self.__nombreContexto = nombreContexto

    # Creando metodos GET Y SET para el numero correspondiente al contexto

    @property
    def contexto(self):
        return self.__contexto
    
    @contexto.setter
    def contexto(self, contexto):
        self.__contexto = contexto

    # Creando metodos GET Y SET para el ID del contexto

    @property
    def idContexto(self):
        return self.__idContexto
    
    @idContexto.setter
    def idContexto(self, idContexto):
        self.__idContexto = idContexto

    # Creando metodos GET Y SET para el numero de linea en donde se hizo una declaracion

    @property
    def linea(self):
        return self.__linea
    
    @linea.setter
    def linea(self, linea):
        self.__linea = linea

    # Creando metodos GET Y SET para la dimension del valor asignado

    @property
    def dimension(self):
        return self.__dimension
    
    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = dimension


    def __str__(self):
        return f"IDENTIFICADOR :  Identificador [ {self.__identificador} ]  Tipo [ {self.__tipo} ]  Valor [ {self.__valor} ]  TipoValor [ {self.__tipoValor} ] nombreContexto [ {self.__nombreContexto} ] Contexto [ {self.__contexto} ]  IdContexto [ {self.__idContexto} ]  Linea [ {self.__linea} ]  Dimension [ {self.__dimension} ]"


tipos_de_datos_identificados = ['cadena', 'entero', 'caracter', 'doble']


def extraer_identificadores_declaraciones(lista_separada, lista_identificada):

    esDeclaracion = False
    tipo = ''
    identificadores = []

    for i in tipos_de_datos_identificados:
        if i == lista_identificada[0]:
            tipo = i
            esDeclaracion = True

    if esDeclaracion:
        for x in range(0, len(lista_identificada)):
            if lista_identificada[x] == 'Identificador' and lista_identificada[x+1] != 'comillas' and lista_identificada[x+1] != 'apostrofe' and lista_identificada[x-1] != 'comillas' and lista_identificada[x-1] != 'apostrofe':
                identificadores.append(lista_separada[x])

    return [tipo, identificadores]


def extraer_valor_de_variables(lista_separada, lista_identificada):

    variables_encontradas = []
    valor_correspondiente = []

    tipoValor = []
    dimension = []

    if len(lista_identificada) >= 3:

        for x in range(0, len(lista_identificada)-1):

            if lista_identificada[x] == 'Identificador' and lista_identificada[x+1] == 'asignacion' and lista_identificada[x+2] == 'Numero':
                variables_encontradas.append(lista_separada[x])
                valor_correspondiente.append(lista_separada[x+2])
                
                if "." in lista_separada[x+2]:
                    tipoValor.append('doble')
                else:
                    tipoValor.append('entero')

                dimension.append(lista_separada[x+2])

    if len(lista_identificada) >= 5:

        for x in range(0, len(lista_identificada)-3):
            
            if lista_identificada[x] == 'Identificador' and lista_identificada[x+1] == 'asignacion' and (lista_identificada[x+2] == 'comillas' or lista_identificada[x+2] == 'apostrofe') and lista_identificada[x+3] == 'Numero' and (lista_identificada[x+4] == 'comillas' or lista_identificada[x+4] == 'apostrofe'):
                variables_encontradas.append(lista_separada[x])
                valor_correspondiente.append(str(lista_separada[x+3]))
                tipoValor.append('cadena')
                dimension.append(str(len(lista_separada[x+3])))
            
            elif lista_identificada[x] == 'Identificador' and lista_identificada[x+1] == 'asignacion' and (lista_identificada[x+2] == 'comillas' or lista_identificada[x+2] == 'apostrofe') and lista_identificada[x+3] == 'Identificador' and (lista_identificada[x+4] == 'comillas' or lista_identificada[x+4] == 'apostrofe'):
                variables_encontradas.append(lista_separada[x])
                valor_correspondiente.append(str(lista_separada[x+3]))

                if len(lista_separada[x+3]) > 1:
                    tipoValor.append('cadena')
                else:
                    tipoValor.append('caracter')

                dimension.append(str(len(lista_separada[x+3])))


    return [variables_encontradas, valor_correspondiente, tipoValor, dimension]



def asignar_nuevos_valores (lista_objetos, lista_ids_asignados, lista_valores_ids, lista_tipoValor, lista_dimensiones):

    for i in range(0, len(lista_objetos)):
        for j in range(0, len(lista_ids_asignados)):
            if lista_objetos[i].identificador == lista_ids_asignados[j]:
                lista_objetos[i].valor = lista_valores_ids[j]
                lista_objetos[i].tipoValor = lista_tipoValor[j]
                lista_objetos[i].dimension = lista_dimensiones[j]


            

