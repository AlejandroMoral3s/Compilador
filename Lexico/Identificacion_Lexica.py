import re

#Funcion que permite identificar si el elemento evaluado es un IDENTIFICADOR
def identificar_ids(elemento):
    patron = '^[a-zA-Z_][a-zA-Z0-9_]*$'
    if(re.search(patron, elemento)):
        return True
    else:
        return False
    
#Funcion que permite identificar si el elemento evaluado es un NUMERO(decimal o entero)
def identificar_numeros(elemento):
    patron = '^\d+(\.\d+)?$'
    if(re.search(patron, elemento)):
        return True
    else:
        return False
    

    


