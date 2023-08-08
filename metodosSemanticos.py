def extraer_declaracion_variables(string_sintactico, lista_separada):

    esDecNumSinVal = False
    esDecNum = False
    esDecLetSinVal = False
    esDecLet = False

    variable = ''
    tipoDeclaracion = ''
    valor = ''
    tipoValor = ''

    decNumSinVal = [
        'entero Identificador punto y coma',
        'doble Identificador punto y coma'
    ]
    decNum = [
        'entero Identificador asignacion Numero punto y coma',
        'doble Identificador asignacion Numero punto y coma'
    ]
    decLetSinVal = [
        'cadena Identificador punto y coma',
        'caracter Identificador punto y coma'
    ]
    decLet = [
        'cadena Identificador asignacion comillas Identificador comillas punto y coma',
        'cadena Identificador asignacion comillas Numero comillas punto y coma',
        'caracter Identificador asignacion apostrofe Identificador apostrofe punto y coma',
    ]

    for x in decNumSinVal:
        if x == string_sintactico:
            esDecNumSinVal = True

    for x in decNum:
        if x == string_sintactico:
            esDecNum = True

    for x in decLetSinVal:
        if x == string_sintactico:
            esDecLetSinVal = True

    for x in decLet:
        if x == string_sintactico:
            esDecLet = True


    if esDecNumSinVal:

        tipoDeclaracion = lista_separada[0]
        variable = lista_separada[1]
        valor = '0'
        tipoValor = lista_separada[0]

    elif esDecNum:

        tipoDeclaracion = lista_separada[0]
        variable = lista_separada[1]
        
        if '.' in lista_separada[3]:
            valor = lista_separada[3]
            tipoValor = 'doble'
        else:
            valor = lista_separada[3]
            tipoValor = 'entero'

    elif esDecLetSinVal:

        tipoDeclaracion = lista_separada[0]
        variable = lista_separada[1]
        tipoValor = lista_separada[0]

    elif esDecLet:

        tipoDeclaracion = lista_separada[0]
        variable = lista_separada[1]
        valor = lista_separada[4]

        if len(lista_separada[4])>1:
            tipoValor = 'cadena'
        elif len(lista_separada) == 1:
            tipoValor = 'caracter'

    return [tipoDeclaracion, variable, valor, tipoValor]
    