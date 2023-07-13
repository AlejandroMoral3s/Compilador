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


Dimensiones_Tipos = {

    'entero': '4',
    'doble': '8',
    'caracter': '1',
    'cadena': '255',
    'booleano': '1'

}

separada = ['bool', 'hola',',','adios', ';']
identificada = ['booleano', 'Identificador','coma', 'Identificador', 'punto y coma']

def devolver_id_y_tipo(lista_separada, lista_identificada):

    lista_id_tipo = []
    iniciaConTipo = False

    for x in Dimensiones_Tipos.keys():
        if x == lista_identificada[0]:
            iniciaConTipo = True
    
    if iniciaConTipo == True:
        for x in range(0, len(lista_separada)):
            if lista_identificada[x] == 'Identificador':
                lista_id_tipo.append(lista_separada[x])
                lista_id_tipo.append(lista_identificada[x])

    iniciaConTipo = False
    return lista_id_tipo

print(devolver_id_y_tipo(separada, identificada))


