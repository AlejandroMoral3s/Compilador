class Identificador:

    def __init__(self, identificador, tipo, contexto, linea, dimension):
        self.__identificador = identificador
        self.__tipo = tipo
        self.__contexto = contexto
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
        self._contexto = contexto

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
        return f"IDENTIFICADOR :  Identificador [ {self.__identificador} ]  Tipo [ {self.__tipo} ]  Contexto [ {self._contexto} ]  Linea [ {self.__linea} ]  Dimension [ {self.__dimension} ]"
    


