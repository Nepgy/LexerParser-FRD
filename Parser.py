from Lexer import tokenizer

estadoActual = {
'tokens': [],
'posicion': 0,
'error': False,
'producciones': [],
'elemento': ''
}

def inicializar(codigoFuente):
    tokens = tokenizer(codigoFuente)
    tokens.append(('$', 'Fin de la cadena'))
    return tokens


def resetEstado(cadena):
    estadoActual['posicion'] = 0
    estadoActual['tokens'] = inicializar(cadena)
    estadoActual['producciones'] = []
    estadoActual['error'] = False
    return estadoActual


def tokenActual():
    return estadoActual['tokens'][estadoActual['posicion']][0]


def pni(noTerminal):
    estadoActual['error'] = True
    parteDerecha = producciones[noTerminal]
    for produccion in parteDerecha:
        estadoActual['error'] = False
        posicionOriginal = estadoActual['posicion']
        procesar(produccion)
        if not estadoActual['error']:
            estadoActual['producciones'].append(produccion)
            break
        estadoActual['posicion'] = posicionOriginal


def procesar(produccion):
    for elemento in produccion:
        if elemento in terminales:
            if elemento == tokenActual():
                estadoActual['posicion'] += 1
            else:
                estadoActual['error'] = True
        if elemento in noTerminales:
            pni(elemento)
        if estadoActual['error']:
            break


def parsing(cadena):
    resetEstado(cadena)
    pni('Funcion')
    if not estadoActual['error']:
        print('Tokens:',estadoActual['tokens'])
        print('Producciones:', estadoActual['producciones'])
        print('Pertenece a la Gramatica')
        return True
    else:
        print('Tokens:', estadoActual['tokens'])
        print('Producciones:', estadoActual['producciones'])
        print('No pertenece a la Gramatica')
        return False

#Terminales
terminales = [
    'INT',
    'IF',
    'IGUALDOB',
    'PAROPEN',
    'COMA',
    'PARCLOSE',
    'LLAOPEN',
    'LLACLOSE',
    'SUMA',
    'ASTERISCO',
    'MINUS',
    'BARRA',
    'PUNCOMA',
    'MENOR',
    'MAYOR',
    'FLOAT',
    'WHILE',
    'FOR',
    'IGUAL',
    'IGUALMAY',
    'IGUALMEN',
    'DIF',
    'ELSE',
    'ID',
    'ERROR_EXPRESION_PARCIAL',
    'NUM',
    'TOKEN_INCORRECTO'
]

#No Terminales
noTerminales = [
    'Funcion',
    'Tipo',
    'ListaArgumento',
    'SentenciaCompuesta',
    'Argumento',
    'Declaracion',
    'ListaIdent',
    'Sentencia',
    'SentFor',
    'SentWhile',
    'Expr',
    'SentIf',
    'ListaSentencia',
    'ValorR',
    'Comparacion',
    'Mag',
    'Termino',
    'X',
    'Factor',
    'Mag2',
    'Termino2'
]

producciones = {
    'Funcion': [
            ['Tipo','ID','PAROPEN','ListaArgumento','PARCLOSE','SentenciaCompuesta']
    ],
    'ListaArgumento': [
            ['Argumento'],
            ['Argumento','COMA','ListaArgumento']
    ],
    'Argumento': [
            ['Tipo','ID']
    ],
    'Declaracion': [
            ['Tipo','ListaIdent']
    ],
    'Tipo': [
            ['INT'],
            ['FLOAT']
    ],
    'ListaIdent': [
            ['ID'],
            ['ID','COMA','ListaIdent']
    ],
    'Sentencia': [
            ['Declaracion'],
            ['SentFor'],
            ['SentWhile'],
            ['Expr'],
            ['SentIf'],
            ['SentenciaCompuesta']
    ],
    'SentFor': [
            ['FOR','PAROPEN','Expr','COMA','Expr','COMA','Expr','PARCLOSE','Sentencia'],
            ['FOR','PAROPEN','Expr','COMA','COMA','Expr','PARCLOSE','Sentencia'],
            ['FOR','PAROPEN','Expr','COMA','Expr','COMA','PARCLOSE','Sentencia'],
            ['FOR','PAROPEN','Expr','COMA','COMA','PARCLOSE','Sentencia']
    ],
    'SentWhile': [
            ['WHILE','PAROPEN','Expr','PARCLOSE','Sentencia']
    ],
    'SentIf': [
            ['IF','PAROPEN','Expr','PARCLOSE','Sentencia','ELSE','PAROPEN','Sentencia','PARCLOSE'],
            ['IF','PAROPEN','Expr','PARCLOSE','Sentencia']
    ],
    'SentenciaCompuesta': [
            ['LLAOPEN','ListaSentencia','LLACLOSE']
    ],
    'ListaSentencia': [
            ['Sentencia'],['Sentencia','ListaSentencia']
    ],
    'Expr': [
            ['ValorR'],
            ['ID','IGUAL','Expr']
    ],
    'ValorR': [
            ['Mag'],
            ['Mag','X']
    ],
    'X': [
            ['Comparacion','Mag'],
            ['Comparacion','Mag','X']
    ],
    'Comparacion': [
            ['IGUALDOB'],
            ['MAYOR'],
            ['MENOR'],
            ['IGUALMAY'],
            ['IGUALMEN'],
            ['DIF']
    ],
    'Mag': [
            ['Termino'],
            ['Termino','Mag2']
    ],
    'Mag2': [
            ['MINUS','Termino'],
            ['SUMA','Termino'],
            ['MINUS','Termino','Mag2'],
            ['SUMA','Termino','Mag2']
    ],
    'Termino': [
            ['Factor'],
            ['Factor','Termino']
    ],
    'Termino2': [
            ['BARRA','Factor'],
            ['ASTERISCO','Factor'],
            ['BARRA','Factor','Termino2'],
            ['ASTERISCO','Factor','Termino2']
    ],
    'Factor': [
            ['NUM'],
            ['ID'],
            ['PAROPEN','Expr','PARCLOSE'],
            ['SUMA','Factor'],
            ['MINUS','Factor']
    ]
    }


#Testing
print('Test 1')
assert parsing('int hola ( float beta ) { 34 }') == True
print('Test 2')
assert parsing('float variable (float var) { if then }') == False
print('Test 3')
assert parsing('int Chocolate == rico') == False
print('Test 4')
assert parsing('float var ( float ab ) { abc }') == True
print('Test 5')
assert parsing('variable int (variable float)') == False
print('Test 6')
assert parsing('float word ( int var ) { while ( 25 ) hola }') == True
print('Test 7')
assert parsing('int a (float hola){ab}') == True
print('Test 8')
assert parsing('int a ( float b ) { int c }') == True
print('Test 9')
assert parsing('int hola ( int var , for ) { 25 }') == False
print('Test 10')
assert parsing('float variable ( int variable ) { float var }') == True
