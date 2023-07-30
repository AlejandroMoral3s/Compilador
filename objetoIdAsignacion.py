class IdentificadorA:

    def __init__(self, identificador, nombreContexto = 'principal', contexto = 0):
        

        self.__identificador = identificador
        self.__nombreContexto = nombreContexto
        self.__contexto = contexto

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

    def __str__(self):
        return f'OBJETO ASIGNACION:  Identificador [ {self.__identificador} ]  NombreContexto [ {self.__nombreContexto} ]  Contexto [ {self.__contexto} ]'