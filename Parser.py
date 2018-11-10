from Lexer import tokenizer

class Parser:
	def __init__(self, terminales, noTerminales):
		self.posicion = 0
		self.error = False
		self.transiciones = []
		self.tokens = []
		self.terminales = terminales
		self.noTerminales = noTerminales
		# self.c = 0

	def pni(self, noTerminal):
		parteDerecha = self.noTerminales[noTerminal]
		posicionOriginal = self.posicion
		for produccion in parteDerecha:
			# print('noTerminal', noTerminal)
			# print('parteDerecha', parteDerecha)
			# if self.c == 50: return None #Debug Purpose
			# self.c += 1
			self.procesar(produccion)
			if self.error:
				self.posicion = posicionOriginal
				# print('error')
				self.error = False
			else:
				self.guardarTransicion(noTerminal, produccion)
				break

		return not self.error

	def procesar(self, produccion):
		# print('produccion', produccion)
		for elemento in produccion:
			# print('elemento', elemento)
			if elemento in self.terminales:
				if elemento == self.getTokenActual():
					# print('OK')
					self.posicion += 1
				else:
					self.error = True
					return False
			else:
				self.pni(elemento)

	def guardarTransicion(self, parteIzquierda, parteDerecha):
		self.transiciones.append((parteIzquierda, parteDerecha))

	def ejecutar(self, tokens, simboloInicial):
		print('tokens', tokens)
		self.tokens = tokens
		return self.pni(simboloInicial)

	def getTokenActual(self):
		return self.tokens[self.posicion][0]

def parsing(cadena):
	parser = Parser(terminales, noTerminales)
	tokens = tokenizer(cadena)
	result = parser.ejecutar(tokens, 'Funcion')
	print(result)
	print(parser.transiciones)
	return result

noTerminales = {
	'Funcion': [
		[
			'Tipo',
			'Id',
			'ParOp',
			'ListaArgumentos',
			'ParCl',
			'SentenciaCompuesta'
		]
	],
	'ListaArgumentos': [
		[
			'Argumento'
		],
		[
			'Argumento',
			'PunctCol',
			'ListaArgumentos',
		]
	],
	'Argumento': [
		[
			'Tipo',
			'Id'
		]
	],
	'Declaracion': [
		[
			'Tipo',
			'ListaIdent'
		]
	],
	'ListaIdent': [
		[
			'Id',
			'PunctCol',
			'ListaIdent'
		],
		[
			'Id'
		]
	],
	'Sentencia': [
		[
			'SentFor'
		],
		[
			'SentWhile'
		],
		[
			'Expr',
			'PunctSemiCol'
		],
		[
			'SentIf'
		],
		[
			'SentenciaCompuesta'
		],
		[
			'Declarcion'
		]
	],
	'SentFor': [
		[
			'LoopFor',
			'ParOp',
			'Expr',
			'PunctCol',
			'Expr',
			'PunctCol',
			'Expr',
			'ParCl',
			'Sentencia'
		],
		[
			'LoopFor',
			'ParOp',
			'Expr',
			'PunctCol',
			'PunctCol',
			'Expr',
			'ParCl',
			'Sentencia'
		],
		[
			'LoopFor',
			'ParOp',
			'Expr',
			'PunctCol',
			'Expr',
			'PunctCol',
			'ParCl',
			'Sentencia'
		],
		[
			'LoopFor',
			'ParOp',
			'Expr',
			'PunctCol',
			'PunctCol',
			'ParCl',
			'Sentencia'
		]
	],
	'SentWhile': [
		[
			'LoopWhile',
			'ParOp',
			'Expr',
			'ParCl',
			'Sentencia'
		]
	],
	'SentIf': [
		[
			'CondIf',
			'ParOp',
			'Expr',
			'ParCl',
			'Sentencia',
			'CondElse',
			'Sentencia'
		],
		[
			'CondIf',
			'ParOp',
			'Expr',
			'ParCl',
			'Sentencia'
		]
	],
	'SentenciaCompuesta': [
		[
			'BrcOp',
			'ListaSentencia',
			'BrcCl'
		],
		[
			'BrcOp',
			'BrcCl'
		]
	],
	'ListaSentencia': [
		[
			'Sentencia',
			'ListaSentencia'
		],
		[
			'Sentencia'
		]
	],
	'Expr': [
		[
			'Id',
			'Asign',
			'Expr'
		],
		[
			'ValorR'
		]
	],
	'ValorR': [
		[
			'Mag',
			'X'
		],
		[
			'Mag'
		]
	],
	'X': [
		[
			'OpRel',
			'Mag',
			'X'
		],
		[
			'OpRel',
			'Mag'
		]
	],
	'Tipo': [
		[
			'TypeInt',
		],
		[
			'TypeFloat'
		]
	],
	'Mag': [
		[
			'Termino',
			'Mag2',
		],
		[
			'Termino'
		]
	],
	'Mag2': [
		[
			'OpMatSubs',
			'Termino',
			'Mag2'
		],
		[
			'OpMatAdd',
			'Termino',
			'Mag2'
		],
		[
			'OpMatAdd',
			'Termino'
		],
		[
			'OpMatSubs',
			'Termino'
		]
	],
	'Termino': [
		[
			'Factor',
			'Termino2'
		],
		[
			'Factor'
		]
	],
	'Termino2': [
		[
			'OpMatDiv',
			'Factor',
			'Termino2'
		],
		[
			'OpMatMult',
			'Factor',
			'Termino2'
		],
		[
			'OpMatDiv',
			'Factor',
		],
		[
			'OpMatMult',
			'Factor',
		]
	],
	'Factor': [
		[
			'ParOp',
			'Expr',
			'ParCl'
		],
		[
			'OpMatAdd',
			'Factor',
		],
		[
			'OpMatSubs',
			'Factor'
		],
		[
			'Num'
		],
		[
			'Id'
		]
	]
}

terminales = [
	'Asign',
	'OpRel',
	'OpMatAdd',
	'OpMatSubs',
	'OpMatMult',
	'OpMatDiv',
	'PunctCol',
	'PunctSemiCol',
	'ParOp',
	'ParCl',
	'BrcOp',
	'BrcCl',
	'CondIf',
	'CondElse',
	'TypeInt',
	'TypeFloat',
	'LoopFor',
	'LoopWhile',
	'Id'
]
