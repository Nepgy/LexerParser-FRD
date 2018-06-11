# class Automata:
#     def __init__(self, tuplaToken):
#         self.tuplaToken = tuplaToken
#         self.estados = []
#         self.estadoInicial = None
#         self.estadoActual = None
#
#         self.crearEstadosNecesarios(tuplaToken[1])
#         self.reset()
#
#     def crearEstadosNecesarios(self, estados):
#         for index, estado in enumerate(estados[::-1]): #Invierto la cadena, para que el primer caracter sea el estado aceptado.
#             if (index == 0):
#                 self.estados.append(Estado(estado, True, None))
#             else:
#                 estadoSiguiente = self.estados[-1]
#                 self.estados.append(Estado(estado, False, (estadoSiguiente.getCodigo(), estadoSiguiente)))
#         estadoSiguiente = self.estados[-1]
#         self.estadoInicial = Estado(estado, False, (estadoSiguiente.getCodigo(), estadoSiguiente))
#
#     def reset(self):
#         self.estadoActual = self.estadoInicial
#
#     def consume(self, char):
#         self.estadoActual = self.estadoActual.input(char)
#
#     def isActualAceptado(self):
#         return self.estadoActual.isAceptado()
#
#     def getTuplaToken(self):
#         return self.tuplaToken
class AutomataBetter:
    def __init__(self, token, estados, estadoInicial, funcionTransicion, estadosAceptados):
        self.token = token
        self.estados = estados
        self.estadoInicial = estadoInicial
        self.funcionTransicion = funcionTransicion
        self.estadoActual = estadoActual
        self.estadosAceptados = estadosAceptados

    def input(self, char):
        self.estadoActual = self.funcionTransicion(char)

    def estadosAceptados(self):
        return self.estadoActual in self.estadosAceptados

    def reset(self):
        self.estadoActual = self.estadoInicial

    def trampa(self):
        return self.estadoActual is None #para identificar el estado trampa





class Estado:
    def __init__(self, codigo, aceptado = False, transiciones = []):
        self.transiciones = transiciones
        self.aceptado = aceptado
        self.codigo = codigo

    def input(self, char):
        if self.transiciones == None:  #Si la transicion es none, significa que es el estado trampa y es su estado siguiente.
            return self
        else:
            return self.getTransicionPara(char) # Devuelve la transicion correspondiente al caracter que recibe. Falta definirla

    def addTransicion(self, tuplaTransicion):
        self.transiciones.append(tuplaTransicion)

    def isAceptado(self):
        return self.aceptado

    def getCodigo(Self):
        return self.codigo

def tokenizer(string): # Todo arranca aca
    automatas = createAutomatas()
    tokens = []
    for char in string:
        for x in automatas:
            if (x.isActualAceptado()):
                tokens.append(x.getTuplaToken())
                for y in automatas:
                    y.reset()
                break
            x.consume(char)

    return tokens


def createAutomatas():
    expresionesReservadas = [("ParOp", "("), ("ParClo", ")"), ("KeyOp", "{"), ("KeyClo", "}"), ("Sum", "+"), ("Mult", "*")] #Estos son solo algunos casos de pruebas
    automatas =[]

    for i in expresionesReservadas:
        automatas.append(Automata(i))

    return automatas

print (tokenizer('{'))


# def lex (src)
#     tokens = []
#     src = src + ""
#     i = 0
#     start = 0
#     state = 0
#     Whille i < len(src):
#         c = src[i]
#         x = src[start: i + 1]
#         if state == 0:
#             if c.isspace():
#                 i +=  1
#                 state = 0
#             else:
#                 start = i
#                 state = 1
#         if state == 1:
#             if es_aceptado(x) or not c.isspace():
#                 i += 1
#                 state = 1
#             else:
#                 i -= 1
#                 state = 2
# #Make spaghetti code
# def es_aceptado(x):
#     candidatos = [TokenType
#         for (TokenType, afd)
#         in TT
#         if afd(x)
#         ]
#     if len(candidatos) > 0
#         return True
#     else:
#         return False
#
# return (True, candidatos[0])
