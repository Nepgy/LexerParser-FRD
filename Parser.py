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
		for coso in produccion:
			if (consume(tokens, produccionesTodas, coso, ParserStatus)):
				ParserStatus.transiciones.append(produccionUsar)
				return True
			else:
				break
	print('ParserStatus.transiciones: ', ParserStatus.transiciones)
	return False


def parser(tokens):
	status = ParserStatus()
	return consume(tokens, definicionProducciones, 'Argumento', status)

definicionProducciones = {
	'Funcion': [
		[
			'Tipo',
			'Identificador',
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
			'Punct',
			'ListaArgumentos',
		]
	],
	'Argumento': [
		[
			'Tipo',
			'Identificador'
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
			'Identificador',
			'Punct',
			'ListaIdent'
		],
		[
			'Identificador'
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
			'Punct'
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
	]
	'Tipo': [
		[
			'Type2', #Cambiar aca y en lexer
			'Type' #Cambiar aca y en lexer
		]
	],
	'ParOp': None,
	'ParCl': None,
	'Identificador': None,
	'Punct': None,
	'Type': None,
	'Type2': [['p']],
	'p': None

}
