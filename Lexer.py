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
        return self.estadoActual is None #para identificar el estado trampa

def transicionDefault(estados, estadoActual, input):

    if estadoActual is None:
        return None

    if len(estados) <= estadoActual + 1:
        return None

    if estados[estadoActual + 1] == input:
        return estadoActual + 1
    else:
        return None

def tokenizer(string): # Todo arranca aca

    automatas = createAutomatas()
    tokens = []
    aceptados = []
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
        print ('--------------------------------------')
        if todosTrampa:
            print(acumuladorInputs)
            print(aceptados)
            print(nuevosAceptados)
            print(tokens)
            if acumuladorInputs == "":
                return "Error"
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

        acumuladorInputs += char.strip()
        aceptados = nuevosAceptados

    return tokens

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


definicionTokens = [
    ("ParOp", "(", transicionDefault),
    ("ParClo", ")", transicionDefault),
    ("KeyOp", "{", transicionDefault),
    ("KeyClo", "}", transicionDefault),
    ("Sum", "+", transicionDefault),
    ("Mult", "*", transicionDefault)
]
