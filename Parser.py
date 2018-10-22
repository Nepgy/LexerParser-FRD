import tokenizer from Lexer

class ParserStatus:
	def __init__(self, posicion = 0, transiciones = []):
		self.posicion = posicion
		self.transiciones = transiciones

def consume(tokens, produccionesTodas, produccionUsar, ParserStatus):
	# ParserStatus.transiciones.append(produccionUsar)
	producciones =  produccionesTodas[produccionUsar]
	if (producciones is None):
		if (produccionUsar == tokens[ParserStatus.posicion][0]):
			ParserStatus.transiciones.append(produccionUsar)
			# ParserStatus.posicion += 1
			return True
		else:
			return False
	for produccion in producciones:
		for termino in produccion:
			if (consume(tokens, produccionesTodas, termino, ParserStatus)):
				ParserStatus.transiciones.append(produccionUsar)
				return True
			else:
				break
	print('ParserStatus.transiciones: ', ParserStatus.transiciones)
	return False


def parser(cadena):
	tokens = tokenizer(cadena)
	status = ParserStatus()
	return consume(tokens, definicionProducciones, 'Argumento', status)

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
