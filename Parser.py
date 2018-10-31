from Lexer import tokenizer

class ParserStatus:
	def __init__(self, posicion = 0, transiciones = []):
		self.posicion = None
		self.transiciones = None
		self.posicionOriginal = posicion
		self.transicionesOriginal = transiciones
		self.reset()

	def reset(self):
		self.posicion = self.posicionOriginal
		self.transiciones = self.transicionesOriginal

def pni(tokens, produccionesGramatica, noTerminalParaEvaluar, ParserStatus):
	posicionOriginal = ParserStatus.posicion
	producciones =  produccionesGramatica[noTerminalParaEvaluar]
	for produccion in producciones:
		estadoProcesar = procesar(tokens, produccionesGramatica, produccion, ParserStatus)
		if estadoProcesar:
			agregarTransicion(ParserStatus, noTerminalParaEvaluar, produccion)
			return True
		else:
			ParserStatus.posicion = posicionOriginal
	return False

def procesar(tokens, produccionesGramatica, produccion, ParserStatus):
	for noTerminal in produccion:
		if esTerminalValido(tokens, produccionesGramatica, noTerminal, ParserStatus):
			return True

		estadoPni = pni(tokens, produccionesGramatica, noTerminal, ParserStatus)
		if estadoPni:
			return True
	return False

def esTerminalValido(tokens, produccionesGramatica, posibleTerminal, parserStatus):
	if (produccionesGramatica[posibleTerminal] is None):
			if (posibleTerminal == tokens[parserStatus.posicion][0]):
				parserStatus.posicion += 1
				return True
	return False

def agregarTransicion(ParserStatus, parteIzq, ParteDer):
	ParserStatus.transiciones.append((parteIzq, ParteDer))

def parser(cadena, status = False):
	if not status:
		status = ParserStatus()
	tokens = tokenizer(cadena)
	return pni(tokens, definicionProducciones, 'Funcion', status)

definicionProducciones = {
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
			'Argumento'
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
	],
	'Asign': None,
	'OpRel': None,
	'OpMatAdd': None,
	'OpMatSubs': None,
	'OpMatMult': None,
	'OpMatDiv': None,
	'PunctCol': None,
	'PunctSemiCol': None,
	'ParOp': None,
	'ParCl': None,
	'BrcOp': None,
	'BrcCl': None,
	'CondIf': None,
	'CondElse': None,
	'TypeInt': None,
	'TypeFloat': None,
	'LoopFor': None,
	'LoopWhile': None,
	'Id': None
}
