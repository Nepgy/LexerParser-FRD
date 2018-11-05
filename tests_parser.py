from Parser import parser, ParserStatus

def test (cadena, resultadoEsperado, transicionesEsperadas):
	status = ParserStatus()
	result = parser(cadena, status)
	print('Cadena de prueba: ', cadena)
	print('Resultado parser:', result)
	print('Resultado espera:', resultadoEsperado)
	print('transiciones parser: ', status.transiciones)
	print('transiciones espera: ', transicionesEsperadas)
	if (result == resultadoEsperado and status.transiciones == transicionesEsperadas):
		print('\033[92mOK')
	else:
		print('\033[91mFALLO')
	print('\033[0m')


test(
	'int funcionAsd ( float argumentoPrueba ) {asd := 5;}',
	True,
	[('asd', 'asd')]
)


