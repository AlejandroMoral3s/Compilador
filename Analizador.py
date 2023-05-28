from Analisis_Lexico import Diccionario


def extract_lines():
    with open('ReceptorLineas.txt', 'r') as f:
        read_data = f.read()

print(Diccionario.cadenas_y_caracteres['comillas'])