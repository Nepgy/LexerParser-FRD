class Automata:
    def __init__(self, identificador, estados, funcionTransicion, estadoAceptado):
        self.identificador = identificador
        self.estados = estados
        self.funcionTransicion = funcionTransicion
        self.estadoAceptado = estadoAceptado
        self.estadoInicial = 0
        self.reset()

    def input(self, char):
        self.estadoActual = self.funcionTransicion(self, char)

    def isAceptado(self):
        return self.estadoActual == self.estadoAceptado

    def reset(self):
        self.estadoActual = self.estadoInicial

    def trampa(self):
        # Se utiliza None para identificar el estado trampa
        return self.estadoActual is None

    def getCharEstado(self, estado):
        if estado is None:
            return None
        else:
            return self.estados[estado]

def transicionDefault(automata, input):

    if automata.estadoActual is None:
        return None

    proximoEstado = automata.estadoActual + 1

    if len(automata.estados) <= proximoEstado:
        return None

    if automata.getCharEstado(proximoEstado) == input:
        return proximoEstado
    else:
        return None

def transicionAlfabetica(automata, input):

    if automata.estadoActual is None:
        return None

    if automata.estadoActual == automata.estadoAceptado:
        if input.isdigit():
            raise Exception('Error')

    if input.isalpha():
        if automata.estadoActual == automata.estadoInicial:
            return automata.estadoActual + 1
        else:
            return automata.estadoActual
    else:
        return None

def transicionNumerica(automata, input):

    if automata.estadoActual is None:
        return None

    if automata.estadoActual == automata.estadoAceptado:
        if input.isalpha():
            raise Exception('Error')

    if input.isdigit():
        if automata.estadoActual == automata.estadoInicial:
            return automata.estadoActual + 1
        else:
            return automata.estadoActual
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
        estadoAceptado = len(definicion[1])
        automatas.append(Automata(idToken, estados, funcionTransicion, estadoAceptado))
    return automatas

#TODO Agregar definiciones de tokens que no utilizan transicionDefault
definicionTokens = [
    ("Asign", "=", transicionDefault),
    ("Asign", ":=", transicionDefault),
    ("OpRel", "<", transicionDefault),
    ("OpRel", ">", transicionDefault),
    ("OpRel", "==", transicionDefault),
    ("OpRel", "!=", transicionDefault),
    ("OpRel", "<=", transicionDefault),
    ("OpRel", ">=", transicionDefault),
    ("OpMat", "+", transicionDefault),
    ("OpMat", "-", transicionDefault),
    ("OpMat", "*", transicionDefault),
    ("OpMat", "/", transicionDefault),
    ("Punct", ",", transicionDefault),
    ("Punct", ";", transicionDefault),
    ("ParOp", "(",transicionDefault),
    ("ParCl", ")",transicionDefault),
    ("BrcOp", "{",transicionDefault),
    ("BrcCl", "}", transicionDefault),
    ("Cond", "if", transicionDefault),
    ("Type", "int", transicionDefault),
    ("Type", "float", transicionDefault),
    ("Loop", "for", transicionDefault),
    ("Loop", "while", transicionDefault),
    ("Id", "a", transicionAlfabetica),
    ("Num", "1", transicionNumerica),
]

