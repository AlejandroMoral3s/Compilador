class Identificador:
    
    def __init__(self, nombre, tipo, dimension, contexto = 0):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__dimension = dimension
        self.__contexto = contexto

    # Getters (Metodos GET)

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def tipo(self):
        return self.__tipo

    @property
    def dimension(self):
        return self.__dimension
    
    @property
    def contexto(self):
        return self.__contexto

    # Setters (Metoos SET)

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = dimension

    @contexto.setter
    def contexto(self, contexto):
        self.__contexto = contexto

        