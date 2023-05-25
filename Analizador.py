from Analisis_Lexico import separadores_Lexico


def extract_lines():
    with open('ReceptorLineas.txt', 'r') as f:
        read_data = f.read()

print(separadores_Lexico.cadenas_y_caracteres['comillas'])