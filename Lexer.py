class Automata:
    def __init__(self, identificador, estados, funcionTransicion, estadosAceptados):
        self.identificador = identificador
        self.estados = estados
        self.funcionTransicion = funcionTransicion
        self.estadosAceptados = estadosAceptados
        self.reset()

    def input(self, char):
        self.estadoActual = self.funcionTransicion(self.estados, self.estadoActual, char)

    def isAceptado(self):
        return self.estadoActual in self.estadosAceptados

    def reset(self):
        self.estadoActual = 0

    def trampa(self):
        # Se utiliza None para identificar el estado trampa
        return self.estadoActual is None

def transicionDefault(estados, estadoActual, input):

    if estadoActual is None:
        return None

    if len(estados) <= estadoActual + 1:
        return None

    if estados[estadoActual + 1] == input:
        return estadoActual + 1
    else:
        return None

def transicionAlfabetica(estados, estadoActual, input):

    if estadoActual is None:
        return None

    if estadoActual != 0:
        if input.isdigit():
            raise Exception('Error')

    if (input.isalpha()):
        if estadoActual == 0:
            return estadoActual + 1
        else:
            return estadoActual
    else:
        return None

def transicionNumerica(estados, estadoActual, input):

    if estadoActual is None:
        return None

    if estadoActual != 0:
        if input.isalpha():
            raise Exception('Error')

    if (input.isdigit()):
        if estadoActual == 0:
            return estadoActual + 1
        else:
            return estadoActual
    else:
        return None


# Todo arranca aca
def tokenizer(string):
    try:
        automatas = createAutomatas()
        tokens = []
        aceptados = []
        # Se agrega un espacio al final de la cadena para generar que todos los automatas caigan
        # al estado trampa antes de terminar la ejecucion del lexer
        string = string + " "
        acumuladorInputs = ""

        for char in string:

            nuevosAceptados = []
            if  acumuladorInputs == "" and char.isspace():
                continue

            for automata in automatas:
                automata.input(char)
                if automata.isAceptado():
                    nuevosAceptados.append(automata)

            todosTrampa = True
            for automata in automatas:
                if not automata.trampa():
                    todosTrampa = False
                    break

            if todosTrampa:
                if acumuladorInputs == "":
                    # return "Error"
                    raise Exception('Error')
                else:

                    tokens.append((aceptados[0].identificador, acumuladorInputs))
                    for automata in automatas:
                        automata.reset()
                    aceptados = []
                    acumuladorInputs = ""

                    if not char.isspace():
                        for automata in automatas:
                            automata.input(char)
                            if automata.isAceptado():
                                nuevosAceptados.append(automata)


            # Se utiliza strip() para no agregar espacios ya que NO es util tenerlos en cuenta a la
            # hora de saber si hemos consumido caracteres luego de haber agregado un token a la lista
            acumuladorInputs += char.strip()
            aceptados = nuevosAceptados

        return tokens
    except Exception as error:
        return str(error)

def createAutomatas():
    automatas = []
    for definicion in definicionTokens:
        idToken = definicion[0]
        # Agrego $ como estado inicial
        estados = '$' + definicion[1]
        funcionTransicion = definicion[2]
        estadosAceptados = [len(definicion[1])]
        automatas.append(Automata(idToken, estados, funcionTransicion, estadosAceptados))
    return automatas

#TODO Agregar definiciones de tokens que no utilizan transicionDefault
definicionTokens = [
    # ("Asign", "=", transicionDefault),
    ("IGUAL", ":=", transicionDefault),
    ("MENOR", "<", transicionDefault),
    ("MAYOR", ">", transicionDefault),
    ("IGUALDOB", "==", transicionDefault),
    ("DIF", "!=", transicionDefault),
    ("IGUALMEN", "<=", transicionDefault),
    ("IGUALMAY", ">=", transicionDefault),
    ("SUMA", "+", transicionDefault),
    ("MINUS", "-", transicionDefault),
    ("ASTERISCO", "*", transicionDefault),
    ("BARRA", "/", transicionDefault),
    ("COMA", ",", transicionDefault),
    ("PUNCOMA", ";", transicionDefault),
    ("PAROPEN", "(",transicionDefault),
    ("PARCLOSE", ")",transicionDefault),
    ("LLAOPEN", "{",transicionDefault),
    ("LLACLOSE", "}", transicionDefault),
    ("IF", "if", transicionDefault),
    ("ELSE", "else", transicionDefault),
    ("INT", "int", transicionDefault),
    ("FLOAT", "float", transicionDefault),
    ("FOR", "for", transicionDefault),
    ("WHILE", "while", transicionDefault),
    ("ID", "a", transicionAlfabetica),
    ("NUM", "1", transicionNumerica),
    # ("ERROR_EXPRESION_PARCIAL",ERROR_EXPRESION_PARCIAL),
    #("TOKEN_INCORRECTO",TOKEN_INCORRECTO)
]
