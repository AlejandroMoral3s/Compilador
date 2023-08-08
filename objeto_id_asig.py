class Identificador:

    def __init__(self, identificador, numeroContexto, linea, nombreContexto = 'principal', tipoDec = 'null', tipoAsig = 'null'):
        self.__identificador = identificador
        self.__tipoDec = tipoDec
        self.__tipoAsig = tipoAsig
        self.__numeroContexto = numeroContexto
        self.__nombreContexto = nombreContexto
        self.__linea = linea

    @property
    def identificador(self):
        return self.__identificador
    
    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def tipoDec(self):
        return self.__tipoDec
    
    @tipoDec.setter
    def tipoDec(self, tipoDec):
        self.__tipoDec = tipoDec

    @property
    def tipoAsig(self):
        return self.__tipoAsig
    
    @tipoAsig.setter
    def tipoAsig(self, tipoAsig):
        self.__tipoAsig = tipoAsig

    @property
    def numeroContexto(self):
        return self.__numeroContexto
    
    @numeroContexto.setter
    def numeroContexto(self, numeroContexto):
        self.__numeroContexto = numeroContexto

    @property
    def nombreContexto(self):
        return self.__nombreContexto
    
    @nombreContexto.setter
    def nombreContexto(self, nombreContexto):
        self.__nombreContexto = nombreContexto  

    @property
    def linea(self):
        return self.__linea
    
    @linea.setter
    def linea(self, linea):
        self.__linea = linea

    def __str__(self):
        return f"IDENTIFICADOR :  Identificador [ {self.__identificador} ]  TipoDec [ {self.__tipoDec} ] TipoAsig [ {self.__Asig} ]  Contexto [ {self.__contexto} ] Linea [ {self.__linea} ]"

