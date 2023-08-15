def extraer_declaracion_variables(string_sintactico, lista_identificada, lista_separada):

    declaracionValida = False

    esDecNumSinVal = False
    esDecNum = False
    esDecLetSinVal = False
    esDecLet = False
    esVarVar = False
    esVarVarClass = False

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
        'doble Identificador asignacion Numero punto y coma',
        'caracter Identificador asignacion Numero punto y coma',
        'cadena Identificador asignacion Numero punto y coma'
    ]
    decLetSinVal = [
        'cadena Identificador punto y coma',
        'caracter Identificador punto y coma'
    ]
    decLet = [
        'cadena Identificador asignacion comillas Identificador comillas punto y coma',
        'cadena Identificador asignacion comillas Numero comillas punto y coma',
        'cadena Identificador asignacion apostrofe Identificador apostrofe punto y coma',
        'cadena Identificador asignacion apostrofe Numero apostrofe punto y coma',

        'caracter Identificador asignacion apostrofe Identificador apostrofe punto y coma',
        'caracter Identificador asignacion apostrofe Numero apostrofe punto y coma',
        'caracter Identificador asignacion comillas Identificador comillas punto y coma',
        'caracter Identificador asignacion comillas Numero comillas punto y coma'
    ]

    decVarVar = [
        'entero Identificador asignacion Identificador punto y coma',
        'doble Identificador asignacion Identificador punto y coma',
        'cadena Identificador asignacion Identificador punto y coma',
        'caracter Identificador asignacion Identificador punto y coma'
    ]

    decVarVarClass = [
        'entero Identificador asignacion llamadoClase Identificador punto y coma',
        'doble Identificador asignacion llamadoClase Identificador punto y coma',
        'cadena Identificador asignacion llamadoClase Identificador punto y coma',
        'caracter Identificador asignacion llamadoClase Identificador punto y coma'
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

    for x in decVarVar:
        if x == string_sintactico:
            esVarVar = True

    for x in decVarVarClass:
        if x == string_sintactico:
            esVarVarClass = True

    if esDecNumSinVal:

        declaracionValida = True
        tipoDeclaracion = lista_identificada[0]
        variable = lista_separada[1]
        valor = '0'
        tipoValor = lista_identificada[0]

    elif esDecNum:

        declaracionValida = True
        tipoDeclaracion = lista_identificada[0]
        variable = lista_separada[1]
        
        if '.' in lista_separada[3]:
            valor = lista_separada[3]
            tipoValor = 'doble'
        else:
            valor = lista_separada[3]
            tipoValor = 'entero'

    elif esDecLetSinVal:

        declaracionValida = True
        tipoDeclaracion = lista_identificada[0]
        variable = lista_separada[1]
        tipoValor = lista_identificada[0]

    elif esDecLet:

        declaracionValida = True
        tipoDeclaracion = lista_identificada[0]
        variable = lista_separada[1]
        valor = lista_separada[4]

        if lista_identificada[3] == "comillas":
            tipoValor = 'cadena'
        else:
            tipoValor = 'caracter'

    elif esVarVar:
        declaracionValida = True
        tipoDeclaracion = lista_identificada[0]
        variable = lista_separada[1]
        valor = lista_separada[3]
        tipoValor = 'VarVar'

    elif esVarVarClass:
        declaracionValida = True
        tipoDeclaracion = lista_identificada[0]
        variable = lista_separada[1]
        valor = lista_separada[4]
        tipoValor = 'VarVarClass'


    if declaracionValida:
        return [tipoDeclaracion, variable, valor, tipoValor]
    else:
        return 0
    

def extraer_asignacion_variables(string_sintactico, lista_separada):
    
    existeAsignacion = False

    environ = ''
    variable = ''
    value = ''
    valueType = ''

    asigNumber = 'Identificador asignacion Numero punto y coma'
    asigNumberClass = 'llamadoClase Identificador asignacion Numero punto y coma'
    
    asigString = 'Identificador asignacion comillas Identificador comillas punto y coma'
    asigStringClass = 'llamadoClase Identificador asignacion comillas Identificador comillas punto y coma'

    asigCharac = 'Identificador asignacion apostrofe Identificador apostrofe punto y coma'
    asigCharacClass = 'llamadoClase Identificador asignacion comillas Identificador comillas punto y coma'

    asigVarVar = 'Identificador asignacion Identificador punto y coma'
    asigVarVarClass = 'llamadoClase Identificador asignacion Identificador punto y coma'

    if string_sintactico == asigNumber:
        
        existeAsignacion = True
        variable = lista_separada[0]
        value = lista_separada[2]
        if '.' in lista_separada[2]:
            valueType = 'doble'
        else:
            valueType = 'entero'

    elif string_sintactico == asigNumberClass:
        
        existeAsignacion = True
        environ = '0'
        variable = lista_separada[1]
        value = lista_separada[3]
        if '.' in lista_separada[3]:
            valueType = 'doble'
        else:
            valueType = 'entero'

    elif string_sintactico == asigString:

        existeAsignacion = True
        variable = lista_separada[0]
        value = lista_separada[3]
        valueType = 'cadena'

    elif string_sintactico == asigStringClass:

        existeAsignacion = True
        environ = '0'
        variable = lista_separada[1]
        value = lista_separada[4]
        valueType = 'cadena'

    elif string_sintactico == asigCharac:

        existeAsignacion = True
        variable = lista_separada[0]
        value = lista_separada[3][0]
        valueType = 'caracter'

    elif string_sintactico == asigCharacClass:

        existeAsignacion = True
        environ = '0'
        variable = lista_separada[1]
        value = lista_separada[4][0]
        valueType = 'cadena'

    elif string_sintactico == asigVarVar:

        existeAsignacion = True
        variable = lista_separada[0]
        value = lista_separada[2]
        valueType = 'VarVar'

    elif string_sintactico == asigVarVarClass:

        environ = '0'
        existeAsignacion = True
        variable = lista_separada[1]
        value = lista_separada[3]
        valueType = 'VarVarClass'

    if existeAsignacion:
        return [environ, variable, value, valueType]
    else:
        return 0


def comparacionTipos(objeto):

    tiposAceptados = False
    nuevoValor = ''
    nuevoTipoValor = ''

    if objeto.tipoDec == objeto.tipoAsig:
        tiposAceptados = True
        nuevoValor = objeto.valor
        nuevoTipoValor = objeto.tipoAsig

        if objeto.tipoDec == 'caracter' and objeto.tipoAsig == 'caracter':
            nuevoValor = objeto.valor[0]
            nuevoTipoValor = 'caracter'

    elif objeto.tipoDec == 'doble' and objeto.tipoAsig == 'entero':

        tiposAceptados = True
        nuevoValor = objeto.valor+'.0'
        nuevoTipoValor = 'doble'

    elif objeto.tipoDec == 'entero' and objeto.tipoAsig == 'doble':

        tiposAceptados = True
        nuevoValor = ''
        for x in objeto.valor:
            if x != '.':
                nuevoValor += x
            else:
                break
        nuevoTipoValor = 'entero'

    elif objeto.tipoDec == 'cadena' and objeto.tipoAsig == 'caracter':
        tiposAceptados = True
        nuevoValor = objeto.valor
        nuevoTipoValor = 'cadena'

    elif objeto.tipoDec == 'caracter' and objeto.tipoAsig == 'entero':
        tiposAceptados = True
        nuevoValor = chr(int(objeto.valor))
        nuevoTipoValor = objeto.tipoDec

    elif objeto.tipoDec == 'caracter' and objeto.tipoAsig == 'doble':
        tiposAceptados = True
        valorTruncado = ''
        for x in objeto.valor:
            if x != '.':
                valorTruncado += x
            else:
                break
        nuevoValor = chr(int(valorTruncado))
        nuevoTipoValor = objeto.tipoDec

    else:
        nuevoValor = objeto.valor
        nuevoTipoValor = objeto.tipoAsig
    

    return [tiposAceptados, nuevoValor, nuevoTipoValor]

    
