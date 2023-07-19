class Identificador:

    def __init__(self, identificador, tipo, contexto, idContexto=0, linea=0, dimension='null'):
        self.__identificador = identificador
        self.__tipo = tipo
        self.__contexto = contexto
        self.__idContexto = idContexto
        self.__linea = linea
        self.__dimension = dimension

    @property
    def identificador(self):
        return self.__identificador
    
    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def contexto(self):
        return self.__contexto
    
    @contexto.setter
    def contexto(self, contexto):
        self.__contexto = contexto

    @property
    def idContexto(self):
        return self.__idContexto
    
    @idContexto.setter
    def idContexto(self, idContexto):
        self.__idContexto = idContexto

    @property
    def linea(self):
        return self.__linea
    
    @linea.setter
    def linea(self, linea):
        self.__linea = linea

    @property
    def dimension(self):
        return self.__dimension
    
    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = dimension

    def __str__(self):
        return f"IDENTIFICADOR :  Identificador [ {self.__identificador} ]  Tipo [ {self.__tipo} ]  Contexto [ {self.__contexto} ]  IdContexto [ {self.__idContexto} ]  Linea [ {self.__linea} ]  Dimension [ {self.__dimension} ]"


tipos_de_datos_identificados = ['cadena', 'entero', 'caracter', 'flotante', 'booleano', 'doble']



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
            if lista_identificada[x] == 'Identificador':
                identificadores.append(lista_separada[x])

    return [tipo, identificadores]


# METODO EN PROCESO
def extraer_valor_de_variables(lista_separada, lista_identificada):

    variables_encontradas = []
    valor_correspondiente = []

    if len(lista_identificada) >= 3:
        for x in range(0, len(lista_identificada)-1):
            if lista_identificada[x] == 'Identificador' and lista_identificada[x+1] == 'asignacion' and lista_identificada[x+2] == 'Numero':
                variables_encontradas.append(lista_separada[x])
                valor_correspondiente.append(lista_separada[x+2])

    return [variables_encontradas, valor_correspondiente]




            

