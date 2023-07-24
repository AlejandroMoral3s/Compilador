class IdentificadorA:

    def __init__(self, identificador, nombreContexto, contexto, linea):
        

        self.__identificador = identificador
        self.__nombreContexto = nombreContexto
        self.__contexto = contexto
        self.__linea = linea

    @property
    def identificador(self):
        return self.__identificador
    
    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def nombreContexto(self):
        return self.__nombreContexto
    
    @nombreContexto.setter
    def nombreContexto(self, nombreContexto):
        self.__nombreContexto = nombreContexto

    @property
    def contexto(self):
        return self.__contexto
    
    @contexto.setter
    def contexto(self, contexto):
        self.__contexto = contexto

    @property
    def linea(self):
        return self.__linea
    
    @linea.setter
    def linea(self, linea):
        self.__linea = linea

    def __str__(self):
        return f'OBJETO ASIGNACION:  Identificador [ {self.__identificador} ]  NombreContexto [ {self.__nombreContexto} ]  Contexto [ {self.__contexto} ]  NoLinea [ {self.__linea} ]'